import sqlite3

# 1. Crear / conectar la base de datos de usuarios
conexion = sqlite3.connect("registro_personas.db")
cursor = conexion.cursor()

# 2. Crear la tabla con restricciones y tipos de datos
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        ciudad TEXT NOT NULL
    )
"""
)
conexion.commit()


# 3. Función para agregar una persona
def agregar_usuario(nombre, edad, ciudad):
    cursor.execute(
        """
        INSERT INTO usuarios (nombre, edad, ciudad)
        VALUES (?, ?, ?)
    """,
        (nombre, edad, ciudad),
    )
    conexion.commit()
    print(f"\n[INFO] {nombre} ha sido agregado exitosamente.")


# 4. Función para mostrar todos los registros
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()

    print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
    if not registros:
        print("La base de datos está vacía.")
    else:
        for u in registros:
            print(f"ID: {u[0]} | Nombre: {u[1]} | Edad: {u[2]} | Ciudad: {u[3]}")
    print("---------------------------------------")


# 5. Función para búsqueda filtrada por ciudad
def buscar_por_ciudad(ciudad_buscar):
    cursor.execute(
        "SELECT * FROM usuarios WHERE LOWER(ciudad) = LOWER(?)",
        (ciudad_buscar,),
    )
    resultados = cursor.fetchall()

    print(f"\n--- RESULTADOS EN: {ciudad_buscar.upper()} ---")
    if not resultados:
        print("No se encontraron personas en esa ciudad.")
    else:
        for u in resultados:
            print(f"ID: {u[0]} | Nombre: {u[1]} | Edad: {u[2]}")
    print("---------------------------------------")


# 6. Control de flujo y menú ejecutable
def main():
    while True:
        print("\n=== GESTOR DE BASE DE DATOS ===")
        print("1. Agregar persona")
        print("2. Ver lista completa")
        print("3. Buscar por ciudad")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            nom = input("Nombre: ").strip()
            try:
                ed = int(input("Edad: "))
                ciu = input("Ciudad: ").strip()
                agregar_usuario(nom, ed, ciu)
            except ValueError:
                print("\n[ERROR] La edad debe ser un número entero.")

        elif opcion == "2":
            listar_usuarios()

        elif opcion == "3":
            ciu_buscar = input("¿Qué ciudad quieres buscar?: ").strip()
            buscar_por_ciudad(ciu_buscar)

        elif opcion == "4":
            print(
                "\nCerrando la sesión y finalizando conexión a la base de datos."
            )
            conexion.close()
            break

        else:
            print(
                "\n[ERROR] Opción no válida. Selecciona un número entre 1 y 4."
            )


if __name__ == "__main__":
    main()
          
