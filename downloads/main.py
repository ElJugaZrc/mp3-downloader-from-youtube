from lector import *
from descargador import *
from convertidor import *
from metadata_changer import *
import os

def main():
    ruta = r"data\urls.txt"
    carpeta = "downloads"
    print("Extrayendo URLs del archivo txt.")
    enlaces = leer_url(ruta)
    for enlace in enlaces:
        datos_cancion = descargar(enlace,carpeta)

        print(f"Convertiendo {datos_cancion.titulo} a mp3...")
        convertir(carpeta, datos_cancion.titulo)
        print("Convertido con éxito")

        print("Eliminando el archivo .webm")
        os.remove(datos_cancion.ruta)      

        print("Editando metadatos de la canción...")
        cambiar_metadata(carpeta, datos_cancion.titulo_mp3, datos_cancion.autor)
        


if __name__ == "__main__":
    main()