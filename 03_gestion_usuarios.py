#================================
# 1. DEFINICIÓN DE FUNCIONES
#================================

def crear_perfil_usuario(nombre, correo, profesion):
    """Limpia los datos y devuelve un diccionario con el perfil del usuario."""
    nombre_limpio = nombre.strip().title()
    correo_limpio = correo.strip().lower()
    profesion_limpio = profesion.strip().title()
    
    perfil = {
        "nombre": nombre_limpio,
        "correo": correo_limpio,
        "profesion": profesion_limpio
    }
    return perfil
    
def mostrar_reporte(lista):
    """Recorre la lista e imprime cada usuario formateado"""
    print("\n--- REPORTE DE USUARIOS ---")
    for usuario in lista:
        print(f"nombre: {usuario['nombre']} | correo: {usuario['correo']} | profesion: {usuario['profesion']}")
        
 #==========================================
# 2. EJECUCIÓN DEL PROGRAMA
#==========================================

#Base de datos vacia
lista_usuarios = []

# Registramos usuario usando .append
u1 = crear_perfil_usuario("Pedrito Pablo", "pedritopablo@mail", "asistente")
lista_usuarios.append(u1)

u2 = crear_perfil_usuario("Pedro Perez", "pedroperez@mail", "Ingeniero")
lista_usuarios.append(u2)

# Imprimimos el reporte ordenado
mostrar_reporte(lista_usuarios)# Mostrar resultados
