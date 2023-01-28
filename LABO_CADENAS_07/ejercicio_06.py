""" Escribir una función que reemplace todas las apariciones
de una subcadena en una cadena dada con otra subcadena dada."""


import re

def reemplazo_palabra(cadena, subcadena, subcadena_cambio):
    return re.sub(subcadena, subcadena_cambio, cadena)


pala = """Un perro muy hambriento caminaba de aquí para allá buscando algo para comer, hasta que un carnicero le tiró un hueso. 
Llevando el hueso en el hocico, tuvo que cruzar un río. Al mirar su reflejo en el agua creyó ver a otro perro con un hueso más grande que el suyo, así que intentó
 arrebatárselo de un solo mordisco. Pero cuando abrió el hocico, el hueso que llevaba cayó al río y se lo llevó la corriente. Muy triste quedó aquel perro al darse cuenta
  de que había soltado algo que era real por perseguir lo que solo era un reflejo."""
subcadena = "Un perro"
subcadena_cambio = " perro (@hotmail.com)"
print(reemplazo_palabra(pala, subcadena, subcadena_cambio))