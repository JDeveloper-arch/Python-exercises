import json
import os

# ==========================================
# 1. CLASS DEFINITION
# ==========================================
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"📦 Product: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock} units")

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"🛒 Sold {quantity} units of {self.name}. Remaining: {self.stock}")
        else:
            print(f"❌ Not enough stock for {self.name}.")

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }


# ==========================================
# 2. VERIFICACIÓN Y CREACIÓN AUTOMÁTICA
# ==========================================
file_name = "inventory.json"

# Si el archivo NO existe en el directorio actual, lo creamos con datos por defecto
if not os.path.exists(file_name):
    default_data = [
        {"name": "Ground Coffee", "price": 5.0, "stock": 20},
        {"name": "Corn Flour", "price": 3.0, "stock": 50}
    ]
    with open(file_name, "w") as file:
        json.dump(default_data, file, indent=4)
    print("⚠️ El archivo no existía, así que fue creado automáticamente con datos iniciales.\n")


# ==========================================
# 3. CARGAR DATOS DESDE EL JSON
# ==========================================
print("--- CARGANDO INVENTARIO DESDE JSON ---")
products_list = []

with open(file_name, "r") as file:
    data = json.load(file)
    for item in data:
        p = Product(item["name"], item["price"], item["stock"])
        products_list.append(p)

for p in products_list:
    p.display_info()


# ==========================================
# 4. INTERACCIÓN Y MODIFICACIÓN
# ==========================================
print("\n--- PROCESANDO VENTA ---")
products_list[0].sell(3)  # Vendemos 3 unidades del primer producto


# ==========================================
# 5. GUARDAR CAMBIOS DE VUELTA EN JSON
# ==========================================
updated_data = [p.to_dict() for p in products_list]

with open(file_name, "w") as file:
    json.dump(updated_data, file, indent=4)

print("\n✅ ¡Cambios guardados con éxito en 'inventory.json'!")
