from typing import NamedTuple
import csv

Cancion = NamedTuple("Cancion", [("url", str), ("titulo", str), ("autor", str), ("album", str)])

def leer_url(ruta: str) -> list[Cancion]:
    res = []
    with open(ruta, encoding="utf-8") as fichero:
        lector = csv.reader(fichero)
        next(lector)
        for url, titulo, autor, album in lector:
            album = None if album == '' else album
            res.append(Cancion(url,titulo,autor,album))
    return res