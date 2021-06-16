import urllib.parse
import requests
import time
import pprint
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "e1H3yoq5lyLXr0ij9Qn23RrBUbTafVri"

while True:
    orig = input("Salida: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destino: ")
    if orig == "quit" or orig == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL:" + (url))
