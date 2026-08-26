import sqlite3

# 1. Conexión a la base de datos local
conexion = sqlite3.connect("alertas_seguridad.db")
cursor = conexion.cursor()

# 2. Creación de la tabla de alertas
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS alertas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origen TEXT NOT NULL,
        monto REAL NOT NULL,
        nivel_riesgo TEXT NOT NULL
    )
"""
)
conexion.commit()


# 3. Función para registrar una nueva alerta
def registrar_alerta(origen, monto, riesgo):
    cursor.execute(
        """
        INSERT INTO alertas (origen, monto, nivel_riesgo)
        VALUES (?, ?, ?)
    """,
        (origen, monto, riesgo),
    )
    conexion.commit()
    print("\n[INFO] Alerta registrada exitosamente en la base de datos.")


# 4. Función para consultar el historial de alertas
def ver_alertas():
    cursor.execute("SELECT * FROM alertas")
    registros = cursor.fetchall()

    print("\n--- HISTORIAL DE ALERTAS REGISTRADAS ---")
    if not registros:
        print("No hay registros en la base de datos.")
    else:
        for r in registros:
            print(
                f"ID: {r[0]} | Origen: {r[1]} | Monto: ${r[2]:.2f} | Riesgo: {r[3]}"
            )
    print("------------------------------------------")


# 5. Control de flujo y menú de consola
def main():
    while True:
        print("\n=== SISTEMA DE GESTIÓN Y CONTROL DE ALERTAS ===")
        print("1. Registrar nueva alerta")
        print("2. Consultar historial de alertas")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            try:
                orig = input("Dirección/Origen de la solicitud: ").strip()
                monto = float(input("Monto detectado ($): "))
                riesgo = (
                    input("Nivel de riesgo (BAJO/MEDIO/ALTO): ")
                    .strip()
                    .upper()
                )
                registrar_alerta(orig, monto, riesgo)
            except ValueError:
                print(
                    "\n[ERROR] Entrada inválida. Ingrese un valor numérico para el monto."
                )

        elif opcion == "2":
            ver_alertas()

        elif opcion == "3":
            print(
                "\nCerrando sesión del sistema y finalizando conexión a la base de datos."
            )
            conexion.close()
            break

        else:
            print(
                "\n[ERROR] Opción no válida. Por favor, seleccione una opción entre 1 y 3."
            )


if __name__ == "__main__":
    main()
