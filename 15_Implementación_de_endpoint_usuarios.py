from fastapi import FastAPI

# Inicialización de la aplicación FastAPI con metadata para la documentación
app = FastAPI(
    title="API de Usuarios",
    description="Servicio web para consultar lista de usuarios.",
    version="1.0.0",
)

# Base de datos simulada (Lista de diccionarios)
base_datos_usuarios = [
    {
        "id": 1,
        "nombre": "Jesus",
        "rol": "Future AI Engineer",
        "edad": 28,
    },
    {
        "id": 2,
        "nombre": "Carlos",
        "rol": "Backend Developer",
        "edad": 30,
    },
]


@app.get("/")
def inicio():
    """Ruta raíz para verificar que el servicio está activo."""
    return {"mensaje": "API de Usuarios activa. Visita /usuarios o /docs"}


@app.get("/usuarios")
def obtener_todos_los_usuarios():
    """Ruta que retorna el listado completo de usuarios en formato JSON."""
    return base_datos_usuarios
