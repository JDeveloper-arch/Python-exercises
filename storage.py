import json
import os
from product import Product

FILE_NAME = "inventory.json"

def load_inventory():
    """Carga los productos desde el archivo JSON."""
    if not os.path.exists(FILE_NAME):
        default_data = [
            {"name": "Ground Coffee", "price": 5.0, "stock": 20},
            {"name": "Corn Flour", "price": 3.0, "stock": 50}
        ]
        with open(FILE_NAME, "w") as f:
            json.dump(default_data, f, indent=4)

    products = []
    with open(FILE_NAME, "r") as f:
        data = json.load(f)
        for item in data:
            products.append(Product(item["name"], item["price"], item["stock"]))
    return products

def save_inventory(products):
    """Guarda la lista de objetos en el archivo JSON."""
    data = [p.to_dict() for p in products]
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ Changes saved successfully to JSON!")
