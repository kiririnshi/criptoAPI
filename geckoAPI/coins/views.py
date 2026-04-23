from datetime import datetime, timezone
from decimal import Decimal
import json
import requests

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

from .models import Moneda, Activo, Precio

API_KEY = 'CG-uUoTUiJ8EebZMvdQqoEdLGHi'
VS_COIN = 'USD'
ACTIVO = 'BTC'
START_DATE = '2026-01-01'
END_DATE = '2026-03-01' # Por ahora no estoy usando la fecha actual, asi que el numero de objetos creados debe mantenerse constante.

def get_graph(request):
    if(request.method == 'GET'):
        moneda, _ = Moneda.objects.update_or_create(nombre = VS_COIN)
        activo, _ = Activo.objects.update_or_create(nombre = ACTIVO)

        precios = (
            Precio.objects
            .filter(moneda=moneda, activo=activo)
            .order_by("fecha_precio")
            .values("fecha_precio", "valor")
        )

        lista_valores = []
        lista_fechas = []

        for precio in precios:
            lista_valores.append(float(precio["valor"]))
            lista_fechas.append(precio["fecha_precio"].strftime("%Y-%m-%d %H:%M:%S"))
        
        context = {
            "fechas": json.dumps(lista_fechas),
            "valores": json.dumps(lista_valores),
        }

        # datetime.datetime not JSON serializable
        # La clase datetime de python no es aceptable para hacer un json, o sea no es json serializable.
        # Por eso es mejor usar strftime para cambiar el formato antes de enviar
        # A su vez pasa algo similar con los valores, json no acepta decimales, asi que se pasan a float para que funcione en ploty.

        return render(request, "coins/index.html", context)
    
        #template = loader.get_template('index.html')
        #return HttpResponse(template.render())
    
def get_all_coins(request):
    if (request.method == 'GET'):
        data = serializers.serialize('json', Precio.objects.all())
        return JsonResponse(json.loads(data), safe=False)

def update_coins(request):
    if (request.method == 'GET'):

        ## Aqui se crean los modelos que deberia ingresar el usuario en la seleccion de moneda.
        ## Nota mental: Esta es la forma perezosa de hacerlo, se deberia cambiar a algo mas elaborado.
        precios_a_crear = []

        moneda, _ = Moneda.objects.update_or_create(nombre = VS_COIN)
        activo, _ = Activo.objects.update_or_create(nombre = ACTIVO)

        url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency={VS_COIN}&from={START_DATE}&to={END_DATE}&x_cg_demo_api_key={API_KEY}"
        
        response = requests.get(url)

        ## Coingeko me da los precios y la fecha de esto, el problema es que la ultima esta en milisegundos y eso no es una informacion relevante para el proyecto.
        ## Asi que se decidio solo obtener el dia y la hora en UTC timezone, por si en el futuro quiero usar esta, pero por ahora solo los dias.

        json_data = json.loads(response.text)
        prices_data = json_data['prices']

        for timestamp_ms, precio in prices_data:
            fecha = datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc)
            precios_a_crear.append(Precio(
                moneda=moneda,
                activo=activo,
                valor=Decimal(str(precio)),  # str() antes de Decimal para evitar imprecisión
                fecha_precio=fecha
        ))

        nuevos_precios = Precio.objects.bulk_create(
            precios_a_crear,
            update_conflicts=True, # Que pasa cuando entra un duplicado? Esto deberia ayudar?
            update_fields=['valor'],
            unique_fields=['moneda', 'activo', 'fecha_precio']
        )

        data = json.loads(serializers.serialize('json', nuevos_precios))
        # send json response with new object
        return JsonResponse(data, safe=False)