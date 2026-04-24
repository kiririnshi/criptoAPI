# criptoAPI version 0.5

## Descripcion

Aplicación Django que consume la API de CoinGecko para almacenar y visualizar precios históricos de criptomonedas.

## Codigo para ejemplo de una request de BTC en coingecko

```python
import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=2026-01-01"
headers = {"x-cg-api-key": "<api-key>"}
response = requests.get(url, headers=headers)
print(response.text)
```

## Tecnologias 

* Python 3.x
* Django
* Ploty

## Instalación

### 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Nada por ahora.

Luego ejecutar:

```bash
python manage.py migrate
```

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

Acceder en:

```
http://127.0.0.1:8000/
```

# Notas del proyecto

[Modelos]
Tres modelos: Moneda, Activo, Precio. Se ven suficientes por ahora para las siguientes versiones.

[Fechas]
Ingresadas por dejecto en el sistema, los dias desde el 1 de enero hasta el 1 de marzo del 2026. 

[Endpoints]

/coins -> Dashboard de graficos
/get_coins -> Punto de consumo, se piden los modelos Precio de la BD.
/update_coins -> Actualiza los valores de los precios en memoria.

# Version 0.5 lista !!! 

## Cosas que faltan para siguiente version.

* Pasar datos a una BD real como Postgresql.
* Usar DRF en vez de las herramientas de Django por defecto en la creacion de APIs.
* Lo ideal seria que el usuario pueda refinar busquedas, tanto por fecha como por moneda y activo.
* Si el usuario elige nuevos activos estos deben ser agregados de manera automatica o podrian estar ya disponibles por defecto.
* Ya en el front deberian verse los filtros con botones y todo eso, tal vez hacer que aparesca el grefico despues de filtrar la busqueda?
* Nuevas busquedas debern quedar grabadas en la BD, el sistema solo muestra lo que tiene, si no lo tiene se busca por API.
* Generar un esquema de pruebas unitarias simples.
* Tareas programadas (cron / Celery) para actualización automática
* Dockerizar una vez que todo este en correcto funcionamiento. 