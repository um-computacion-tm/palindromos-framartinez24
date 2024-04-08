# import unittest

# from palindrome import palindrome

# class TestIsPalindrome(unittest.TestCase):
#     def test_with_a(self):
#         value = "a"
#         result = palindrome(value)
#         self.assertTrue(result)

#     def test_with_ala(self):
#         value = "ala"
#         result = palindrome(value)
#         self.assertTrue(result)

#     def test_with_neuquen(self):
#         value = "neuquen"
#         result = palindrome(value)
#         self.assertTrue(result)

#     def test_with_hola(self):
#         value = "hola"
#         result = palindrome(value)
#         self.assertFalse(result)
    
#     def test_with_panqueua(self):
#         value = "panqueua"
#         result = palindrome(value)
#         self.assertFalse(result)

#     def test_with_anitalavalatina(self):
#         value = "anitalavalatina"
#         result = palindrome(value)
#         self.assertTrue(result)

#     def test_with_oso(self):
#         value = "oso"
#         result = palindrome(value)
#         self.assertTrue(result)

#     def test_with_Lachamba(self):
#         value = "LaChambaMeEstáMatando"
#         result = palindrome(value)
#         self.assertFalse(result)

# if __name__ == "__main__":
#     unittest.main()


import unittest
from palindrome import obtener_cantidad_de_palabras_palindrome 
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input_str = "a"  # Renombra la variable de entrada para evitar conflicto con la función input
        result = is_palindrome(input_str)
        self.assertTrue(result)

    def test_with_ala(self):
        input_str = "ala"
        result = is_palindrome(input_str)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input_str = "neuquen"
        result = is_palindrome(input_str)
        self.assertTrue(result)

    def test_with_hola(self):
        input_str = "hola"
        result = is_palindrome(input_str)
        self.assertFalse(result)



class TestCantidadDePalabrasPalindromes(unittest.TestCase):
    
    def test_cantidad_de_palabras_palindromes_simple(self):
        palabras = ["ala"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 1)
 
    def test_cantidad_de_palabras_palindromes_con_2(self):
        palabras = ["ala", "neuquen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)
 
    def test_cantidad_de_palabras_palindromes_con_3(self):
        palabras = ["ala", "neuquen", "hola"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)
 
    def test_cantidad_de_palabras_palindromes_con_4(self):
        palabras = ["ala", "neuquen", "hola", "programacion"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 2)
 
    def test_cantidad_de_palabras_palindromes_con_5(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 3)


    def test_cantidad_de_palabras_palindromes_con_6(self):
        palabras = ["la", "chamba", "te", "destruye", "el", "corazon"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 0)


 
    def test_cantidad_de_palabras_palindromes_complejo(self):
        palabras = ["ala", "neuquen", "hola", "programacion", "palap", "neu  quen"]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 4)
 
    def test_cantidad_de_palabras_palindromes_complejo_2(self):
        palabras = [
             "ala",
             "neuquen",
             "hola",
             "programacion",
             "palap",
             "neu  quen",
             "agita falsos usos la fatiga",
             "presidente de la camara de diputados: martin menem",
             "Con Menem me hice la casa"
        ]
        resultado = obtener_cantidad_de_palabras_palindrome(palabras)
        self.assertEqual(resultado, 5)

if __name__ == '__main__':  
    unittest.main()