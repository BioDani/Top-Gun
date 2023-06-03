import unittest

def sumar(a, b):
    return a + b 

# Debe llamarse la clase Test y el archivo test al inicio, así es que lo reconoce unittest. 
class TestSumar(unittest.TestCase):
    def test_sumar_dos_numeros_positivos(self):
        result = sumar(3, 2)
        self.assertEqual(result, 5)
    
    def test_sumar_dos_numeros_negativos(self):
        result = sumar(-3, -2)
        self.assertEqual(result, -5)


# Ejecutar como: python -m unitest