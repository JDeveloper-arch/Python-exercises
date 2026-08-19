import json
import os
from product import Product

FILE_NAME = "inventory.json"

def load_inventory():
    """Carga los productos desde el archivo JSON usando List Comprehension."""
    if not os.path.exists(FILE_NAME):
        default_data = [
            {"name": "Ground Coffee", "price": 5.0, "stock": 20, "history": []},
            {"name": "Corn Flour", "price": 3.0, "stock": 4, "history": []}
        ]
        with open(FILE_NAME, "w") as f:
            json.dump(default_data, f, indent=4)

    with open(FILE_NAME, "r") as f:
        data = json.load(f)
        # List comprehension para instanciar objetos en una sola línea
        return [Product(item["name"], item["price"], item["stock"], item.get("history", [])) for item in data]

def save_inventory(products):
    """Guarda la lista de objetos usando List Comprehension."""
    data = [p.to_dict() for p in products]
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ Changes saved successfully!")
