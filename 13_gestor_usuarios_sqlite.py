import sqlite3

# 1. Configuración de la conexión y cursor a la base de datos
conexion = sqlite3.connect("registro_personas.db")
cursor = conexion.cursor()

# 2. Inicialización del esquema de la tabla de usuarios
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


# 3. Operación CREATE: Inserción de un nuevo registro
def agregar_usuario(nombre: str, edad: int, ciudad: str) -> None:
    cursor.execute(
        """
        INSERT INTO usuarios (nombre, edad, ciudad)
        VALUES (?, ?, ?)
        """,
        (nombre, edad, ciudad),
    )
    conexion.commit()
    print(f"\n[INFO] {nombre} ha sido registrado exitosamente.")


# 4. Operación READ: Lectura global de la tabla
def listar_usuarios() -> None:
    cursor.execute("SELECT * FROM usuarios")
    registros = cursor.fetchall()

    print("\n--- REGISTRO GENERAL DE USUARIOS ---")
    if not registros:
        print("La base de datos no contiene registros.")
    else:
        for u in registros:
            print(f"ID: {u[0]} | Nombre: {u[1]} | Edad: {u[2]} | Ciudad: {u[3]}")
    print("-----------------------------------")


# 5. Operación READ (Filtrada): Consulta por criterio de ciudad
def buscar_por_ciudad(ciudad_buscar: str) -> None:
    cursor.execute(
        "SELECT * FROM usuarios WHERE LOWER(ciudad) = LOWER(?)",
        (ciudad_buscar,),
    )
    resultados = cursor.fetchall()

    print(f"\n--- CONSULTA DE REGISTROS EN: {ciudad_buscar.upper()} ---")
    if not resultados:
        print("No se encontraron coincidencias para la ciudad especificada.")
    else:
        for u in resultados:
            print(f"ID: {u[0]} | Nombre: {u[1]} | Edad: {u[2]}")
    print("-----------------------------------")


# 6. Operación DELETE: Eliminación de un registro por identificador único
def eliminar_usuario(id_usuario: int) -> None:
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
    existe = cursor.fetchone()

    if not existe:
        print(f"\n[ERROR] No existe ningún registro asignado al ID {id_usuario}.")
    else:
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conexion.commit()
        print(f"\n[INFO] Registro con ID {id_usuario} eliminado correctamente.")


# 7. Operación UPDATE: Actualización de datos por identificador único
def actualizar_usuario(id_usuario: int) -> None:
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
    existe = cursor.fetchone()

    if not existe:
        print(f"\n[ERROR] No existe ningún registro asignado al ID {id_usuario}.")
    else:
        print(f"\n--- ACTUALIZACIÓN DE DATOS (ID: {id_usuario} - {existe[1]}) ---")
        nuevo_nombre = input("Nuevo nombre: ").strip()
        try:
            nueva_edad = int(input("Nueva edad: "))
            nueva_ciudad = input("Nueva ciudad: ").strip()

            cursor.execute(
                """
                UPDATE usuarios
                SET nombre = ?, edad = ?, ciudad = ?
                WHERE id = ?
                """,
                (nuevo_nombre, nueva_edad, nueva_ciudad, id_usuario),
            )
            conexion.commit()
            print(f"\n[INFO] Registro con ID {id_usuario} actualizado con éxito.")
        except ValueError:
            print("\n[ERROR] Formato inválido. La edad debe ser un entero.")


# 8. Interfaz de consola para el control de flujo
def main() -> None:
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE BASE DE DATOS (CRUD) ===")
        print("1. Agregar usuario (CREATE)")
        print("2. Listar todos los usuarios (READ)")
        print("3. Buscar usuarios por ciudad (READ - Filtered)")
        print("4. Eliminar usuario por ID (DELETE)")
        print("5. Actualizar usuario por ID (UPDATE)")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ").strip()

        if opcion == "1":
            nom = input("Nombre: ").strip()
            try:
                ed = int(input("Edad: "))
                ciu = input("Ciudad: ").strip()
                agregar_usuario(nom, ed, ciu)
            except ValueError:
                print("\n[ERROR] Formato inválido. La edad debe ser un entero.")

        elif opcion == "2":
            listar_usuarios()

        elif opcion == "3":
            ciu_buscar = input("Ingrese la ciudad a consultar: ").strip()
            buscar_por_ciudad(ciu_buscar)

        elif opcion == "4":
            try:
                id_borrar = int(input("Ingrese el ID del registro a eliminar: "))
                eliminar_usuario(id_borrar)
            except ValueError:
                print("\n[ERROR] Formato inválido. El ID debe ser un entero.")

        elif opcion == "5":
            try:
                id_modificar = int(input("Ingrese el ID del registro a actualizar: "))
                actualizar_usuario(id_modificar)
            except ValueError:
                print("\n[ERROR] Formato inválido. El ID debe ser un entero.")

        elif opcion == "6":
            print("\nCerrando la sesión y finalizando conexión a la base de datos...")
            conexion.close()
            break

        else:
            print("\n[ERROR] Opción no válida. Selecciona un valor entre 1 y 6.")


if __name__ == "__main__":
    main()
  
