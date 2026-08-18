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
            return True
        else:
            print(f"❌ Not enough stock for {self.name}. Available: {self.stock}")
            return False

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

         