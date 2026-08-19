from product import Product
from storage import load_inventory, save_inventory

def main():
    products = load_inventory()

    while True:
        print("\n=== ADVANCED INVENTORY SYSTEM ===")
        print("1. View all products")
        print("2. Sell a product")
        print("3. Add new product")
        print("4. Low stock alert (< 5 units)")
        print("5. Save and Exit")
        
        option = input("\nSelect an option (1-5): ").strip()

        if option == "1":
            print("\n--- CURRENT INVENTORY ---")
            for p in products:
                p.display_info()
                if p.history:
                    print(f"   📜 History: {p.history[-1]}") # Muestra la última venta

        elif option == "2":
            print("\n--- SELL PRODUCT ---")
            name_to_sell = input("Enter product name: ").strip()
            found = False
            
            for p in products:
                if p.name.lower() == name_to_sell.lower():
                    found = True
                    try:
                        qty = int(input(f"Enter quantity of '{p.name}' to sell: "))
                        p.sell(qty)
                    except ValueError:
                        print("❌ Invalid input!")
                    break
            
            if not found:
                print(f"❌ Product '{name_to_sell}' not found.")

        elif option == "3":
            print("\n--- ADD NEW PRODUCT ---")
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter price ($): "))
                stock = int(input("Enter initial stock: "))
                products.append(Product(name, price, stock))
                print(f"✅ Product '{name}' added!")
            except ValueError:
                print("❌ Invalid input!")

        elif option == "4":
            print("\n--- LOW STOCK ALERT (< 5 units) ---")
            # Filtro con lambda: extrae solo los productos con stock menor a 5
            low_stock = list(filter(lambda p: p.stock < 5, products))
            
            if low_stock:
                for p in low_stock:
                    print(f"⚠️ RESTOCK NEEDED: {p.name} (Only {p.stock} units remaining)")
            else:
                print("✅ All products have sufficient stock!")

        elif option == "5":
            save_inventory(products)
            print("👋 Exiting program. See you later!")
            break

        else:
            print("❌ Invalid option!")

if __name__ == "__main__":
    main()
