import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def cambiar_metadata(carpeta, archivo, autor) -> None:
    ruta = os.path.join(carpeta, archivo)

    try:
        try:
            tags = EasyID3(ruta)
        except:
            mp3 = MP3(ruta)
            mp3.add_tags()
            mp3.save()
            tags = EasyID3(ruta)
        # Guardamos solo lo que pida el usuario
        if autor:
            tags["artist"] = autor
        tags.save()
        print("Metadatos guardados correctamente.")
    except Exception as e:
        print(f"Error editando metadatos: {e}")