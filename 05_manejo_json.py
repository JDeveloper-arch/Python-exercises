import json

# ==========================================
# 1. INVENTARIO INICIAL Y GUARDADO
# ==========================================
inventario = [
    {"nombre": "harina", "precio": 1.20},
    {"nombre": "pan", "precio": 0.90},
    {"nombre": "queso", "precio": 2.99},
    {"nombre": "carne", "precio": 4.00}
]

# Guardamos el inventario inicial por primera vez
with open("inventario.json", "w") as archivo:
    json.dump(inventario, archivo, indent=4)

print("✅ Inventario inicial guardado.")


# ==========================================
# 2. LEER DESDE EL ARCHIVO JSON
# ==========================================
with open("inventario.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print("\n--- 📦 DATOS LEÍDOS DEL ARCHIVO ---")
print(datos_cargados)


# ==========================================
# 3. AGREGAR PRODUCTO NUEVO Y REGUARDAR
# ==========================================
# A. Creamos el nuevo producto (en la memoria RAM)
nuevo_producto = {"nombre": "pescado", "precio": 3.50}

# B. Se lo agregamos a la lista que leímos antes
datos_cargados.append(nuevo_producto)

# C. Vuelves a abrir el archivo para sobrescribirlo con la lista actualizada
with open("inventario.json", "w") as archivo:
    json.dump(datos_cargados, archivo, indent=4)

print("\n✅ ¡Pescado agregado y guardado en el archivo!")


# ==========================================
# 4. COMPROBACIÓN FINAL (Lectura)
# ==========================================
with open("inventario.json", "r") as archivo:
    inventario_final = json.load(archivo)

print("\n--- 🛒 INVENTARIO FINAL ACTUALIZADO ---")
print(inventario_final)
