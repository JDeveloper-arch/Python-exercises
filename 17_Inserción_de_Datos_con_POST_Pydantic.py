import sqlite3
from typing import Dict, List, Union
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Inicialización y metadata OpenAPI para Swagger
app = FastAPI(
    title="API de Gestión de Usuarios - SQLite3",
    description="Servicio Backend en FastAPI para la lectura e inserción de datos validados en SQLite.",
    version="1.0.0",
)

# Constante global para la base de datos
DB_NAME = "registro_personas.db"


# ==========================================
# MODELOS DE DATOS (Pydantic Schemes)
# ==========================================
class UsuarioCrear(BaseModel):
    """Esquema de Pydantic para la validación del payload recibido en peticiones POST."""

    nombre: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Nombre completo del usuario",
    )
    edad: int = Field(
        ..., gt=0, lt=120, description="Edad del usuario en años cumplidos"
    )

    class Config:
        json_schema_extra = {
            "example": {"nombre": "Carlos Mendoza", "edad": 25}
        }


# ==========================================
# FUNCIONES AUXILIARES DE BASE DE DATOS
# ==========================================
def inicializar_db() -> None:
    """Garantiza la creación del archivo de base de datos y la tabla objetivo (DDL)

    si no existen al iniciar el servicio.
    """
    with sqlite3.connect(DB_NAME) as conexion:
        cursor = conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL
            )
        """
        )
        conexion.commit()


# Se ejecuta la inicialización de la DB al cargar el módulo
inicializar_db()


# ==========================================
# ENDPOINTS REST (API Routes)
# ==========================================
@app.get(
    "/db-usuarios",
    response_model=List[Dict[str, Union[int, str]]],
    status_code=status.HTTP_200_OK,
    summary="Obtener todos los usuarios",
)
def listar_usuarios():
    """Consulta la base de datos relacional y retorna todos los registros

    transformados a una estructura serializable JSON.
    """
    try:
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, edad FROM personas")
            filas = cursor.fetchall()

        usuarios = [
            {"id": fila[0], "nombre": fila[1], "edad": fila[2]} for fila in filas
        ]
        return usuarios

    except sqlite3.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al consultar la base de datos: {str(e)}",
        )


@app.post(
    "/db-usuarios",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo usuario",
)
def crear_usuario(usuario: UsuarioCrear):
    """Recibe un JSON validado mediante Pydantic, ejecuta la inserción (DML)

    de forma segura e inserta el nuevo registro en SQLite.
    """
    try:
        with sqlite3.connect(DB_NAME) as conexion:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO personas (nombre, edad) VALUES (?, ?)",
                (usuario.nombre, usuario.edad),
            )
            conexion.commit()
            nuevo_id = cursor.lastrowid

        return {
            "mensaje": "Usuario creado exitosamente",
            "usuario": {
                "id": nuevo_id,
                "nombre": usuario.nombre,
                "edad": usuario.edad,
            },
        }

    except sqlite3.Error as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al insertar en la base de datos: {str(e)}",
        )
        
