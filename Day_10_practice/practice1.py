import json

product = {
    "name": "Laptop",
    "price": 85000,
    "category": "Electronics"
}

with open ("product.json", "w") as file:
    json.dump(product, file)

with open ("product.json", "r") as file:
   loaded_product = json.load(file)
print(loaded_product["name"])