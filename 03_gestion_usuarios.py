"""
Módulo de Gestión de Usuarios
-----------------------------
Este script limpia, da formato y registra perfiles de usuarios 
almacenándolos como diccionarios dentro de una lista estructurada.
"""

def crear_perfil_usuario(nombre, correo, profesion):
    """Limpia los datos de entrada y devuelve un diccionario con el perfil del usuario."""
    nombre_limpio = nombre.strip().title()
    correo_limpio = correo.strip().lower()
    profesion_limpia = profesion.strip().title()

    perfil = {
        "nombre": nombre_limpio,
        "correo": correo_limpio,
        "profesion": profesion_limpia
    }
    
    return perfil


# ==========================================
# EJECUCIÓN PRINCIPAL DEL PROGRAMA
# ==========================================

# Base de datos de usuarios
lista_usuarios = []

# Registro de usuarios
usuario1 = crear_perfil_usuario(" JUAN PEREZ", "juanperez@mail", "programador")
lista_usuarios.append(usuario1)

usuario2 = crear_perfil_usuario(" PEDRO PEREZ", "pedroperez@mail", "Arquitecto")
lista_usuarios.append(usuario2)

# Mostrar resultados
print(f"Usuarios registrados exitosamente:\n{lista_usuarios}")
