import unittest

def is_palindrome(value):
    for indice in range(len(value) // 2): 
        reverse = -(indice + 1)
        if value[indice] != value[reverse]:
            return False
    return True


def obtener_cantidad_de_palabras_palindrome(palabras):
    contador = 0
    for palabra in palabras:
        palabra = palabra.replace(" ", "").replace(":", "").replace("-", "").lower() 
        if palabra == palabra[::-1]:
            contador += 1
    return contador