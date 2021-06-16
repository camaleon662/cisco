import urllib.parse
import requests
import time
import pprint
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "e1H3yoq5lyLXr0ij9Qn23RrBUbTafVri"

while True:
    orig = input("Salida: ")
    dest = input("Destino: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL:" + (url))
