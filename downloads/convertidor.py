from ffmpeg import FFmpeg
import os

def convertir(carpeta: str,archivo: str) -> None:
    ruta = os.path.join(carpeta, archivo)
    base, ext = os.path.splitext(ruta)
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(ruta)
        .output(
            f"{base}.mp3"
        )
    )
    ffmpeg.execute()