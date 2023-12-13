import json
import requests

data_url = "https://dummyjson.com/quotes?limit=100"

source_data = requests.get(url=data_url)
data = source_data.json()

with open("data.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
