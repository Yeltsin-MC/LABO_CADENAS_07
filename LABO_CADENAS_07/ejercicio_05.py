"""Escribir una función que determine la longitud de la
subcadena más larga que contiene solo dígitos."""


def subcadena_larga(palabra):
    subcadenas = palabra.split()
    lista_cadenas = []
    for i in subcadenas:
        lista_cadenas.append(len(i))
    for j in subcadenas:
        if len(j) == max(lista_cadenas):
            return str(i) + " <-- : de valor : " + str(len(j))


print("La cadena mas larga es --> "+subcadena_larga("Nosotros somos estudiantes de la escuela ingenieria de sistemas"))