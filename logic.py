
alumnos = ["Juan", "Alejandra"]

cinturon_por_alumno = {}


def obtener_cinturon(kihon: int, katas: int, kumite: int, mental: int) -> str:
    if (kihon == 1) and (katas == 1) and (kumite == 1) and (mental == 1):
        return "Blanco"
    elif (kihon == 2) and (katas == 2) and (kumite == 2) and (mental == 2):
        return "Amarillo"
    elif (kihon == 3) and (katas == 3) and (kumite == 3) and (mental == 3):
        return "Naranja"
    elif (kihon == 4) and (katas == 4) and (kumite == 4) and (mental == 4):
        return "Verde"
    elif (kihon == 5) and (katas == 5) and (kumite == 5) and (mental == 5):
        return "Azul"
    elif (kihon == 6) and (katas == 6) and (kumite == 6) and (mental == 6):
        return "Marrón"
    elif (kihon == 7) and (katas == 7) and (kumite == 7) and (mental == 7):
        return "Negro"
    else:
        return "No califica para un cinturón estándar"
