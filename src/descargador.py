from pytubefix import YouTube
from typing import NamedTuple
from liampia_nombre import *

Rutas = NamedTuple("Rutas", [("mp3", str), ("webm", str)])

def descargar(url: str, carpeta: str, titulo: str) -> Rutas:
    yt = YouTube(url)
    # Creamos el stream de audio
    stream_audio = yt.streams.filter(only_audio=True).first()
    print("Iniciando descarga:")
    try:
        ruta_webm = stream_audio.download(output_path=carpeta,filename=titulo)
        print(f"Descarga completada con éxito! Audio descargado: {titulo}")
        return Rutas(f"{titulo}.mp3", ruta_webm)
    except Exception as e:
        print(f"Ha ocurrido un error mientras se realizaba la descarga: {e}")