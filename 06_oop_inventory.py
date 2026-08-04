# ==========================================
# 1. CLASS DEFINITION (El Molde / Plantilla)
# ==========================================
class Product:
    # Constructor: Inicializa las propiedades básicas de cada producto
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Método para mostrar el estado actual del producto en consola
    def display_info(self):
        print(f"📦 Product: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock} units")

    # Método para aplicar un porcentaje de descuento al precio
    def apply_discount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price -= discount
        print(f"🏷️ Discount applied: {percentage}% off (${discount:.2f}) on {self.name}.")

    # Método para procesar ventas y descontar del inventario
    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"🛒 Sold: {quantity} unit(s) of {self.name}. Remaining stock: {self.stock}")
        else:
            print(f"❌ Transaction failed: Not enough stock for {self.name}. Requested: {quantity}, Available: {self.stock}")


# ==========================================
# 2. OBJECT INSTANTIATION (Creación y Uso)
# ==========================================

# Creación de objetos independientes usando la clase Product
product_1 = Product("Ground Coffee", 5.00, 20)
product_2 = Product("Corn Flour", 3.00, 50)

print("--- INITIAL INVENTORY STATE ---")
product_1.display_info()
product_2.display_info()

print("\n--- PROCESSING DISCOUNT ---")
product_1.apply_discount(20)  # Aplica 20% de descuento al café

print("\n--- PROCESSING SALE ---")
product_1.sell(5)  # Vende 5 unidades de café

print("\n--- FINAL INVENTORY STATE ---")
product_1.display_info()
