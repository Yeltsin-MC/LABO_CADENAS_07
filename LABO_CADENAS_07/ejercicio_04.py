"""Escribir una función que determine la frecuencia de cada
carácter en una cadena dada y devuelva un diccionario."""


def Diccionario_texto(texto):
    retirar = ".;:.\n\"'"    #hacemos que los siguientes signos de puntuacion o caracteres sean reemplazados por un espacio
    for i in retirar:
        texto = texto.replace(i,"")    #lo reemplaza
    texto.lower()
    list_palabras = texto.split(" ")
    diccionario = {}
    for i in list_palabras:
        if i in diccionario:
            diccionario[i] += 1 # contadores
        else:
            diccionario[i] = 1
    for j in diccionario:
        cantidad = diccionario[j]
        print(f"Palabra {j} se repite {cantidad}")
Diccionario_texto("""Un perro muy hambriento caminaba de aquí para allá buscando algo para comer, hasta que un carnicero le tiró un hueso. 
Llevando el hueso en el hocico, tuvo que cruzar un río. Al mirar su reflejo en el agua creyó ver a otro perro con un hueso más grande que el suyo, así que intentó
 arrebatárselo de un solo mordisco. Pero cuando abrió el hocico, el hueso que llevaba cayó al río y se lo llevó la corriente. Muy triste quedó aquel perro al darse cuenta
  de que había soltado algo que era real por perseguir lo que solo era un reflejo.""")