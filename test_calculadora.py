# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair, potencia, calcular_media


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar(self):
        """Testa se a função somar está funcionando corretamente."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa se a função subtrair está funcionando corretamente."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        """Testa se a função multiplicar está funcionando corretamente."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        """Testa se a função dividir está funcionando corretamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero gera erro."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 2), 4)
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(3, 4), 81)

    def test_calcular_media(self):
        """Testa se a função calcular_media está funcionando corretamente."""
        # 1. Lista com números inteiros
        self.assertEqual(calcular_media([10, 8, 6]), 8)
        
        # 2. Lista com números decimais
        self.assertEqual(calcular_media([7.5, 2.5, 5.0]), 5.0)
        
        # 3. Lista com apenas um número
        self.assertEqual(calcular_media([15]), 15)
        
        # 4. Lista vazia (deve gerar ValueError)
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_multiplicar_inteiros_positivos(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(7, 0), 0)
        self.assertEqual(multiplicar(0, 5), 0)

    def test_multiplicar_negativo_e_positivo(self):
        self.assertEqual(multiplicar(-4, 5), -20)

    def test_multiplicar_dois_negativos(self):
        self.assertEqual(multiplicar(-3, -6), 18)

    def test_multiplicar_decimais(self):
        self.assertAlmostEqual(multiplicar(1.5, 2.0), 3.0)

    def test_multiplicar_entrada_nao_numerica_gera_typeerror(self):
        with self.assertRaises(TypeError):
            multiplicar("a", "b")

    def test_divisao_exata(self):
        self.assertEqual(dividir(6, 3), 2)

    def test_divisao_com_resultado_decimal(self):
        self.assertEqual(dividir(5, 2), 2.5)

    def test_divisao_numero_negativo(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_divisao_zero_por_outro_numero(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_divisao_por_zero_deve_levantar_erro(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_divisao_precisao_repeticao_decimal(self):
        self.assertAlmostEqual(dividir(1, 3), 0.3333333333333333)

    def test_divisao_entradas_nao_numericas_gera_typeerror(self):
        with self.assertRaises(TypeError):
            dividir("a", 2)

    def test_divisao_dois_negativos(self):
        self.assertEqual(dividir(-9, -3), 3)


if __name__ == "__main__":
    unittest.main()
