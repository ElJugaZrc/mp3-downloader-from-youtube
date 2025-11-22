import re

def limpiar_nombre(nombre: str) -> str:
    # Reemplaza caracteres ilegales de Windows y Unicode raros
    nombre = re.sub(r'[<>:"/\\|?*\u2022]', '', nombre)
    nombre = nombre.strip()
    return nombre