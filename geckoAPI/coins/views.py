from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json
import requests

from .models import Moneda, Activo, Precio

API_KEY = 'CG-uUoTUiJ8EebZMvdQqoEdLGHi'
VS_COIN = 'USD'
START_DATE = '2026-01-01'
END_DATE = '2026-03-01'

def get_coins(request):
    if (request.method == 'GET'):
        data = serializers.serialize('json', Precio.objects.all())
        return JsonResponse(json.loads(data), safe=False)

def update_coins(request):
    if (request.method == 'GET'):

        url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency={VS_COIN}&from={START_DATE}&to={END_DATE}&x_cg_demo_api_key={API_KEY}"
        
        response = requests.get(url)

        #data = serializers.serialize('json', Precio.objects.all())
        #return JsonResponse(json.loads(data), safe=False)
        return JsonResponse(json.loads(response.text))