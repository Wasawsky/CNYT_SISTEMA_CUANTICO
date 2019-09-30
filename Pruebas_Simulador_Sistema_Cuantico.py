import unittest
import Simulador_Sistema_Cuantico

class Prueba_Simulador(unittest.TestCase):
    def test_detectarParticula(self):
        self.assertEqual(Simulador_Sistema_Cuantico.detectarParticula([(-3.0, -1.0), (0.0, -2.0), (0.0, 1.0), (2.0, 0.0)],2),0.05263157894736841)
    def test_rransitarVector(self):
        self.assertEqual(Simulador_Sistema_Cuantico.transitarVector([(1.0, 0.0), (0.0, -1.0)],[(0.0, 1.0), (1.0, 0.0)]),(0.0, -2.0))    

if __name__ == "__main__":
    unittest.main()
	
	
