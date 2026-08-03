# ==========================================
# 1. INVENTARIO DE LA TIENDA
# ==========================================

# Lista de diccionarios con productos y precios
inventario = [
    {"nombre": "harina", "precio": 1.20},
    {"nombre": "pan", "precio": 0.90},
    {"nombre": "queso", "precio": 2.99},
    {"nombre": "carne", "precio": 4.00}
]

# Función para mostrar los productos
def mostrar_inventario(lista_productos):
    print("\n--- 📦 PRODUCTOS DISPONIBLES ---")
    for i, producto in enumerate(lista_productos, start=1):
        print(f"{i}. {producto['nombre']} -> ${producto['precio']:.2f}")

# ==========================================
# 2. FUNCIÓN PARA CALCULAR EL TOTAL
# ==========================================

def calcular_total(carrito):
    total = 0
    for producto in carrito:
        total += producto['precio']  # Va sumando el precio a cada ítem
    return total

# ==========================================
# 3. MENÚ PRINCIPAL E INTERACCIÓN
# ==========================================

carrito = []

while True:
    print("\n--- 🏪 MENÚ DE OPCIONES ---")
    print("1. Ver lista de productos")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito y pagar")
    print("4. Salir")
    
    opcion = input("\nElige una opción (1-4): ")
    
    if opcion == "1":
        mostrar_inventario(inventario)
        
    elif opcion == "2":
        mostrar_inventario(inventario)
        
        # Atrapamos el error si el usuario escribe letras en lugar de números
        try:
            eleccion = int(input("\nEscribe el número del producto que deseas agregar: "))
            indice = eleccion - 1  # Restamos 1 porque las listas empiezan en 0
            
            if 0 <= indice < len(inventario):
                producto_elegido = inventario[indice]
                carrito.append(producto_elegido)
                print(f"✅ ¡{producto_elegido['nombre']} agregado al carrito!")
            else:
                print("❌ Número de producto inválido.")
                
        except ValueError:
            print("❌ Error: Debes ingresar un número (ejemplo: 1, 2, 3).")
            
    elif opcion == "3":
        if len(carrito) == 0:
            print("\n🛒 Tu carrito está vacío.")
        else:
            print("\n--- 🛒 TU CARRITO ---")
            for item in carrito:
                print(f"- {item['nombre']}: ${item['precio']:.2f}")
            
            total_a_pagar = calcular_total(carrito)
            print(f"\n💵 Total a pagar: ${total_a_pagar:.2f}")
            
    elif opcion == "4":
        print("\n👋 ¡Gracias por tu compra! Hasta luego.")
        break  # Rompe el bucle y cierra el programa
        
    else:
        print("❌ Opción inválida. Intenta de nuevo.")
          
