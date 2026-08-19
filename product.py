from datetime import datetime

class Product:
    def __init__(self, name, price, stock, history=None):
        self.name = name
        self.price = price
        self.stock = stock
        # Si no viene historial, creamos una lista vacía
        self.history = history if history is not None else []

    def display_info(self):
        print(f"📦 Product: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock} units")

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            # Generamos la estampa de tiempo actual en formato AAAA-MM-DD HH:MM
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            log_entry = f"[{timestamp}] Sold {quantity} units"
            self.history.append(log_entry)
            
            print(f"🛒 Sold {quantity} units of {self.name}. Remaining: {self.stock}")
            return True
        else:
            print(f"❌ Not enough stock for {self.name}. Available: {self.stock}")
            return False

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "history": self.history
        }         
