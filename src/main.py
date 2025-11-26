from lector import *
from descargador import *
from convertidor import *
from metadata_changer import *
import os

def main():
    ruta = r"data\urls.csv"
    carpeta = "downloads"
    print("Extrayendo URLs del archivo txt.")
    canciones = leer_url(ruta)
    for cancion in canciones:
        rutas = descargar(cancion.url,carpeta,cancion.titulo)

        print(f"Convertiendo {cancion.titulo} a mp3...")
        convertir(carpeta, cancion.titulo)
        print("Convertido con éxito")

        print("Eliminando el archivo .webm")
        os.remove(rutas.webm)      

        print("Editando metadatos de la canción...")
        cambiar_metadata(carpeta, rutas.mp3, cancion.titulo, cancion.autor, cancion.album)
        


if __name__ == "__main__":
    main()