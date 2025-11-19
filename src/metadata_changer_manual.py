# Archivo que uso para cambiar el autor a mano en caso de que el que haya puesto no me gusta
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def main():
    carpeta = "downloads"

    # Comprobamos que la carpeta existe
    if not os.path.isdir(carpeta):
        print("La carpeta no existe.")
        return

    # Recorremos todos los archivos
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith(".mp3"):
            ruta = os.path.join(carpeta, archivo)

            print(f"\n--- Editando: {archivo} ---")

            # Pedimos metadatos al usuario
            artista = input("Autor/Artista (deja vacío para no cambiar): ").strip()

            # Abrimos el archivo MP3
            try:
                try:
                    tags = EasyID3(ruta)
                except:
                    mp3 = MP3(ruta)
                    mp3.add_tags()
                    mp3.save()
                    tags = EasyID3(ruta)

                # Guardamos solo lo que pida el usuario
                if artista:
                    tags["artist"] = artista
                tags.save()
                print("Metadatos guardados correctamente.")

            except Exception as e:
                print(f"Error editando metadatos: {e}")

    print("\nProceso completado.")

if __name__ == "__main__":
    main()