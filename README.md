# criptoAPI

Aplicación Django que consume la API de CoinGecko para almacenar y visualizar precios históricos de criptomonedas.

# Codigo para ejemplo de una request de BTC en coingecko

import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=2026-01-01"

headers = {"x-cg-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)


# Notas de uso

[Modelos]
Tres modelos: Moneda, Activo, Precio. 

[Fechas]
La idea seria que el usuario pueda ingresar la fecha de un calendario y otros parametros para refinar busquedas.
Por ahora la aplicacion solo toma fechas pre fijadas por el programador, desde el 1 de enero hasta el 1 de marzo.

[Endpoints]

La api de graficos solo necesita un endpoint que me de todos los puntos del grafico precio x fecha, o sea leer los modelos de Precio en BD. 
Tambien se añadio un endpoint para actualizar los contenidos de los modelos, en caso de que se añadan mas precios.