
alumnos = ["Juan", "Alejandra"]

cinturon_por_alumno = {}


def obtener_cinturon(kihon: int, katas: int, kumite: int, mental: int) -> str:
    puntaje = (kihon * 0.2) + (katas * 0.3) + (kumite * 0.3) + (mental * 0.2)
    
    if puntaje >= 6.5:
        return "Negro"
    elif puntaje >= 5.5:
        return "Marrón"
    elif puntaje >= 4.5:
        return "Azul"
    elif puntaje >= 3.5:
        return "Verde"
    elif puntaje >= 2.5:
        return "Naranja"
    elif puntaje >= 1.5:
        return "Amarillo"
    else:
        return "Blanco"
