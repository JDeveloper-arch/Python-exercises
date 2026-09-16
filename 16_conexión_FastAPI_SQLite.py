import sqlite3
from fastapi import FastAPI

# Inicialización de la aplicación FastAPI con metadata para la documentación OpenAPI
app = FastAPI(
    title="API de usuarios con SQLite",
    description="Servicio web para consultar datos persistentes desde una base de datos SQLite.",
    version="1.0.0",
)

# Nombre de la base de datos local
DB_NAME = "registro_personas.db"


def obtener_usuarios_db():
    """Conecta a la base de datos SQLite, asegura la existencia de la tabla

    e información inicial, y retorna todos los registros formateados.
    """
    # 1. Establecer conexión con el archivo de la base de datos
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()

    # 2. Garantizar la estructura de la tabla (DDL)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER
        )
    """
    )

    # 3. Insertar un registro inicial de prueba si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM personas")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO personas (nombre, edad) VALUES ('Jesus', 28)"
        )
        conexion.commit()

    # 4. Consultar los registros existentes
    cursor.execute("SELECT id, nombre, edad FROM personas")
    filas = cursor.fetchall()

    # 5. Cerrar la conexión para liberar recursos
    conexion.close()

    # 6. Mapear las tuplas de SQLite a una lista de diccionarios (compatibles con JSON)
    usuarios = []
    for fila in filas:
        usuarios.append({"id": fila[0], "nombre": fila[1], "edad": fila[2]})

    return usuarios


@app.get("/")
def inicio():
    """Ruta raíz para verificar la disponibilidad del servicio."""
    return {"mensaje": "API conectada a SQLite y activa"}


@app.get("/db-usuarios")
def listar_usuarios_base_datos():
    """Endpoint REST que retorna el listado de usuarios desde la base de datos."""
    return obtener_usuarios_db()
    
