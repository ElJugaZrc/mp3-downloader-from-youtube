def leer_url(ruta: str) -> list[str]:
    res = []
    with open(ruta, encoding="utf-8") as fichero:
        for enlace in fichero:
            res.append(enlace[:-1])
    return res