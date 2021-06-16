import urllib.parse
import requests
import time
import pprint
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "e1H3yoq5lyLXr0ij9Qn23RrBUbTafVri"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()

print(url)

json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

# para poder ver mejor el json por consola
# pprint.pprint(json_data)
