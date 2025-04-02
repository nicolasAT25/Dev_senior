import sys
import os
from src.negocio import VendedorBase, VendedorPremium
import unittest

# Funciona aún cuando comento esta línea
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

class TestVendedor(unittest.TestCase):
    def setUp(self):
        self.vendedor_base = VendedorBase("Fernando", 1000)
        self.vendedor_premium = VendedorPremium("Nicolás", 5000)
        
    def test_calcular_comision_base(self):
        self.assertEqual(self.vendedor_base.calcular_comision(), 100)
        
    def test_calcular_comision_premium(self):
        self.assertEqual(self.vendedor_premium.calcular_comision(), 750)
        
if __name__ == "__main__":
    unittest.main()