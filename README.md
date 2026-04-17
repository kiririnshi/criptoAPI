# criptoAPI
A simple connection to a cripto bros api

# Codigo para ejemplo de una request de BTC en coingecko

import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=2026-01-01"

headers = {"x-cg-api-key": "<api-key>"}

response = requests.get(url, headers=headers)

print(response.text)

# La idea seria que el usuario pueda ingresar la fecha de un calendario y otros parametros para refinar busquedas.