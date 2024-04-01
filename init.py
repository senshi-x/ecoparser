import requests
import json

data_store = requests.get("https://white-tiger.play.eco/api/v1/plugins/EcoPriceCalculator/stores").json()
print(json.dumps(data_store, indent=4, sort_keys=True))