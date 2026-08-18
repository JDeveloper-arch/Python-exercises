from product import Product
from storage import load_inventory

def main():
    products = load.inventory()
    
    while True:
        print("\n=== MODULAR INVENTORY SYSTEM ===")
        print("1. View all products")
        print("2. Sell a product")
        print("3. Add new product")
        print("4. Save and Exit")
        
        option = input("\nSelect an option (1-4): ").strip()

        if option == "1":
            print("\n--- CURRENT INVENTORY ---")
            for p in products:
                p.display_info()

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
                        print("❌ Invalid input! Please enter a number.")
                    break
            
            if not found:
                print(f"❌ Product '{name_to_sell}' not found in inventory.")

        elif option == "3":
            print("\n--- ADD NEW PRODUCT ---")
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter price ($): "))
                stock = int(input("Enter initial stock: "))
                new_product = Product(name, price, stock)
                products.append(new_product)
                print(f"✅ Product '{name}' added successfully!")
            except ValueError:
                print("❌ Invalid input! Price must be a number and stock an integer.")

        elif option == "4":
            save_inventory(products)
            print("👋 Exiting program. See you later!")
            break

        else:
            print("❌ Invalid option! Please select between 1 and 4.")

if __name__ == "__main__":
    main()