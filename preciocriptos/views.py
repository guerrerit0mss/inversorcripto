from django.shortcuts import render
import requests
import json

# Create your views here.

def apis (request):
   
   
    url1="https://criptoya.com/api/bitso/btc/usd"
    url2="https://api.binance.com/api/v1/ticker/price?symbol=ETHUSDT"

    precio1=requests.get(url1).json()
    precio2=requests.get(url2).json()

    formateado1=round(float(precio2["price"]),2)


    criptos={"BTC":30000, "ETH":5000, "precio2":formateado1,  "precio1":precio1["ask"]}


    return render(request, "cabecera.html",criptos)
