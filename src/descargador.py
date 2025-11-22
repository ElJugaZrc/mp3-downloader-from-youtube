from pytubefix import YouTube
from typing import NamedTuple
from liampia_nombre import *

Cancion = NamedTuple("Cancion", [("titulo", str), ("autor", str), ("ruta", str), ("titulo_mp3", str)])

def descargar(url: str, carpeta: str) -> Cancion:
    yt = YouTube(url)
    tittle_original = f"{yt.title}"
    tittle = limpiar_nombre(tittle_original)
    author = yt.author
    # Creamos el stream de audio
    stream_audio = yt.streams.filter(only_audio=True).first()
    print("Iniciando descarga:")
    try:
        ruta_webm = stream_audio.download(output_path=carpeta,filename=tittle)
        print(f"Descarga completada con éxito! Audio descargado: {tittle}")
        return Cancion(tittle, author, ruta_webm, f"{tittle}.mp3")
    except Exception as e:
        print(f"Ha ocurrido un error mientras se realizaba la descarga: ")