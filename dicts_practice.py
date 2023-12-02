import requests

url_carts = "https://dummyjson.com/carts"

carts_from_net = requests.get(url=url_carts)
data = carts_from_net.json()
carts = data["carts"]

for cart in carts:
    if cart["userId"] == 56:
        for product in cart["products"]:
            if product["discountPercentage"] > 15:
                print(product["title"])
