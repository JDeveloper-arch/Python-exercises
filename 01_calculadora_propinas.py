# ==========================================
# Ejercicio 01: Calculadora de Propinas
# Descripción: Script interactivo para calcular propinas,
# registrar el historial de cuentas y obtener métricas con listas.
# ==========================================

# 1. Creamos la lista vacía para almacenar el historial de montos finales
historial_cuentas = []
calcular_otra_cuenta = "si"

# 2. Bucle principal para registrar múltiples cuentas
while calcular_otra_cuenta == "si":
    print("\n--- NUEVA CUENTA ---")
    
    # Pedimos los datos del cliente y la cuenta
    nombre = input("Ingresa tu nombre: ")
    monto_total = float(input("Ingresa el monto total: "))
    porcentaje_propina = float(input("Ingresa el porcentaje de propina (10, 20, 30): "))

    # Evaluamos la generosidad de la propina
    if porcentaje_propina >= 15:
        print("¡Eres muy generoso, gracias por la propina!")
    else:
        print("Propina estándar registrada.")

    # Operaciones matemáticas
    monto_propina = monto_total * (porcentaje_propina / 100)
    monto_final = monto_total + monto_propina

    # Guardamos el monto final en nuestro historial usando .append()
    historial_cuentas.append(monto_final)

    # Mostramos el desglose de la cuenta actual
    print(f"Hola {nombre}, el total de la propina es ${monto_propina} y el monto total a pagar es: ${monto_final}. ¡Gracias por su compra!")
    
    # Preguntamos al usuario si desea continuar en el bucle
    calcular_otra_cuenta = input("\n¿Deseas calcular otra cuenta? (si/no): ")

# 3. Resumen y métricas del historial de ventas
print("\n--- RESUMEN DEL DÍA ---")
print(f"Historial de montos finales: {historial_cuentas}")
print(f"Se procesaron en total: {len(historial_cuentas)} cuentas.")

# Uso de funciones de listas (sum, max, min)
print(f"Total ingresado en el día: ${sum(historial_cuentas)}")
print(f"La venta más alta fue: ${max(historial_cuentas)}")
print(f"La venta más baja fue: ${min(historial_cuentas)}")

print("\nPrograma finalizado. ¡Hasta luego!")
