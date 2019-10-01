#Version 2.0
import unittest
from Calculadora import *

class Pruebaa(unittest.TestCase):
    
    def test_suma(self):
        a=Calculadora()
        self.assertEqual(a.suma((3,-1),(1,4)),(4,3))
    def test_resta(self):
        a=Calculadora()
        self.assertEqual(a.resta((3,-1),(1,4)),(2,-5))
    def test_multiplicacion(self):
        a=Calculadora()
        self.assertEqual(a.multiplicacion((3,-1),(1,4)),(7,11))
    def test_multiplicacioncuadradoComplejo(self):
        a=Calculadora()
        self.assertEqual(a.multiplicacion((0,1),(0,1)),(-1,0))
    def test_division(self):
        a=Calculadora()
        self.assertEqual(a.division((-2,1),(1,2)),(0.0,1.0))
    def test_modulo(self):
        a=Calculadora()
        self.assertEqual(a.modulo((1,-1)),1.4142135623730951)
    def test_conjugado(self):
        a=Calculadora()
        self.assertEqual(a.conjugado((1,-1)),(1,1))
    def test_fase(self):
        a=Calculadora()
        self.assertEqual(a.fase((1,1)),(45.0))
    def test_convpolaracartesiano(self):
        a=Calculadora()
        self.assertEqual(a.convpolaracartesiano((3.16,108.43)),(-0.999020803757226,2.9979255217000085))
    def test_convcartesianoapolar(self):
        a=Calculadora()
        self.assertEqual(a.convcartesianoapolar((1,1)),(1.4142135623730951,45.0))
    def test_sumaVectores(self):
        a=Calculadora()
        self.assertEqual(a.sumaVectores([(6.0, -4.0), (7.0, 3.0), (4.2, -8.1), (0.0, -3.0)],[(16.0, 2.3), (0.0, -7.0), (6.0, 0.0), (0.0, -4.0)]),[(22.0, -1.7000000000000002), (7.0, -4.0), (10.2, -8.1), (0.0, -7.0)])
    def test_sumaVectoresImposible(self):
        a=Calculadora()
        self.assertEqual(a.sumaVectores([(6.0, -4.0), (7.0, 3.0), (4.2, -8.1), (0.0, -3.0)],[(16.0, 2.3), (0.0, -7.0), (6.0, 0.0)]),"Imposible")
    def test_inversa(self):
        a=Calculadora()
        self.assertEqual(a.inversa([(6.0, -4.0), (7.0, 3.0), (4.2, -8.1), (0.0, -3.0)]),[(-6.0, 4.0), (-7.0, -3.0), (-4.2, 8.1), (0.0, 3.0)])
    def test_multiplicacionEscalarVector(self):
        a=Calculadora()
        self.assertEqual(a.multiplicacionEscalarVector([(6.0, 3.0), (0.0, 0.0), (5.0, 1.0), (4.0, 0.0)],(3.0, 2.0)),[(12.0, 21.0), (0.0, 0.0), (13.0, 13.0), (12.0, 8.0)])
    def test_sumaMatrices(self):
        a=Calculadora()
        self.assertEqual(a.sumaMatrices([[(6.0, -4.0), (6.0, -4.0)], [(7.0, 3.0), (7.0, 3.0)]],[[(4.2, -8.1), (4.2, -8.1)], [(0.0, -3.0), (0.0, -3.0)]]),[[(10.2, -12.1), (10.2, -12.1)], [(7.0, 0.0), (7.0, 0.0)]])
    def test_sumaMatricesImposible(self):
        a=Calculadora()
        self.assertEqual(a.sumaMatrices([[(6.0, -4.0), (6.0, -4.0)], [(7.0, 3.0), (7.0, 3.0)]],[[(4.2, -8.1), (4.2, -8.1)]]),"Imposible")
    def test_inversaMatriz(self):
        a=Calculadora()
        self.assertEqual(a.inversaMatriz([[(16.0, 2.3), (16.0, 2.3)], [(0.0, -7.0), (0.0, -7.0)], [(6.0, 0.0), (6.0, 0.0)], [(0.0, -4.0), (0.0, -4.0)]]),[[(-16.0, -2.3), (-16.0, -2.3)], [(0.0, 7.0), (0.0, 7.0)], [(-6.0, 0.0), (-6.0, 0.0)], [(0.0, 4.0), (0.0, 4.0)]])
    def test_multiplicacionEscalarMatriz(self):
        a=Calculadora()
        self.assertEqual(a.multiplicacionEscalarMatriz([[(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)], [(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)]],(4.0, 0.0)),[[(4.0, -8.0), (8.0, 12.0)], [(12.0, 16.0), (16.0, -20.0)], [(4.0, -8.0), (8.0, 12.0)], [(12.0, 16.0), (16.0, -20.0)]])
    def test_transpuesta(self):
        a=Calculadora()
        self.assertEqual(a.transpuesta([[(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)], [(1.0, -2.0), (2.0, 3.0)], [(3.0, 4.0), (4.0, -5.0)]]),[[(1.0, -2.0), (3.0, 4.0), (1.0, -2.0), (3.0, 4.0)], [(2.0, 3.0), (4.0, -5.0), (2.0, 3.0), (4.0, -5.0)]])
    def test_matrizConjugada(self):
        a=Calculadora()
        self.assertEqual(a.matrizConjugada([[(1.0, -2.0), (2.0, 3.0), (4.0, 5.0)], [(3.0, 4.0), (4.0, -5.0), (5.0, 6.0)], [(1.0, -2.0), (2.0, 3.0), (7.0, 8.0)]]),[[(1.0, 2.0), (2.0, -3.0), (4.0, -5.0)], [(3.0, -4.0), (4.0, 5.0), (5.0, -6.0)], [(1.0, 2.0), (2.0, -3.0), (7.0, -8.0)]])
    def test_matrizAdjunta(self):
        a=Calculadora()
        self.assertEqual(a.matrizAdjunta([[(1.0, -2.0), (2.0, 3.0), (4.0, 5.0)], [(3.0, 4.0), (4.0, -5.0), (5.0, 6.0)], [(1.0, -2.0), (2.0, 3.0), (7.0, 8.0)]]),[[(1.0, 2.0), (3.0, -4.0), (1.0, 2.0)], [(2.0, -3.0), (4.0, 5.0), (2.0, -3.0)], [(4.0, -5.0), (5.0, -6.0), (7.0, -8.0)]])
    def test_multiplicacionMatrizMatriz(self):
        a=Calculadora()
        self.assertEqual(a.multiplicacionMatrizMatriz([[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)], [(1.0, 0.0), (4.0, 2.0), (0.0, 1.0)], [(4.0, -1.0), (0.0, 0.0), (4.0, 0.0)]],[[(5.0, 0.0), (2.0, -1.0), (6.0, -4.0)], [(0.0, 0.0), (4.0, 5.0), (2.0, 0.0)], [(7.0, -4.0), (2.0, 7.0), (0.0, 0.0)]]),[[(26.0, -52.0), (60.0, 24.0), (26.0, 0.0)], [(9.0, 7.0), (1.0, 29.0), (14.0, 0.0)], [(48.0, -21.0), (15.0, 22.0), (20.0, -22.0)]])
    def test_multiplicacionMatrizMatrizImposible(self):
        a=Calculadora()
        self.assertEqual(a.multiplicacionMatrizMatriz([[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)], [(1.0, 0.0), (4.0, 2.0), (0.0, 1.0)], [(4.0, -1.0), (0.0, 0.0), (4.0, 0.0)]],[[(5.0, 0.0), (2.0, -1.0), (6.0, -4.0)], [(0.0, 0.0), (4.0, 5.0), (2.0, 0.0)]]),"Imposible")
    def test_accion(self):
        a=Calculadora()
        self.assertEqual(a.accion([[(1.0, 0.0), (4.0, 2.0), (0.0, 1.0)], [(4.0, -1.0), (0.0, 0.0), (4.0, 0.0)], [(5.0, 0.0), (2.0, -1.0), (6.0, -4.0)]],[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)]),[[(9.0, 7.0)], [(34.0, -19.0)], [(21.0, -46.0)]])
    def test_accionImposible(self):
        a=Calculadora()
        self.assertEqual(a.accion([[(1.0, 0.0), (4.0, 2.0)], [(4.0, -1.0), (0.0, 0.0)], [(5.0, 0.0), (2.0, -1.0)]],[(3.0, 2.0), (0.0, 0.0), (5.0, -6.0)]),"Imposible")
    def test_sumaDiagonal(self):
        a=Calculadora()
        self.assertEqual(a.sumaDiagonal([[(1.0, 0.0), (0.0, 0.0), (0.0, 0.0)], [(0.0, 0.0), (1.0, 0.0), (0.0, 0.0)], [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0)]]),(3.0, 0.0))
    def test_productoInternoMatriz(self):
        a=Calculadora()
        self.assertEqual(a.productoInternoMatriz([[(1.0, 0.0), (-1.0, 0.0)], [(1.0, 0.0), (1.0, 0.0)]],[[(2.0, 0.0), (1.0, 0.0)], [(1.0, 0.0), (3.0, 0.0)]]),(5.0, 0.0))
    def test_normaMatriz(self):
        a=Calculadora()
        self.assertEqual(a.normaMatriz([[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]]),9.16515138991168)
    def test_distanciaMatrizMatriz(self):
        a=Calculadora()
        self.assertEqual(a.distanciaMatrizMatriz([[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]],[[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]]),0.0)
    def test_distanciaMatrizMatrizImposible(self):
        a=Calculadora()
        self.assertEqual(a.distanciaMatrizMatriz([[(3.0, 2.0), (2.0, 4.0)]],[[(3.0, 2.0), (2.0, 4.0)], [(1.0, 3.0), (4.0, 5.0)]]),"Imposible")
    def test_matrizIdentidad(self):
        a=Calculadora()
        self.assertEqual(a.matrizIdentidad(3),[[(1, 0), (0, 0), (0, 0)], [(0, 0), (1, 0), (0, 0)], [(0, 0), (0, 0), (1, 0)]])
    def test_matrizUnitaria(self):
        a=Calculadora()
        self.assertEqual(a.matrizUnitaria([[(0.0, 0.0), (0.0, 1.0)], [(0.0, -1.0), (0.0, 0.0)]]),True)
    def test_matrizUnitariaNoes(self):
        a=Calculadora()
        self.assertEqual(a.matrizUnitaria([[(0.0, 0.0), (2.4, 1.0)], [(0.0, 1.0), (0.0, 3.5)]]),False)
    def test_matrizUnitariaImposible(self):
        a=Calculadora()
        self.assertEqual(a.matrizUnitaria([[(0.0, 0.0), (0.0, 1.0)], [(0.0, -1.0), (0.0, 0.0)],[(0.0, -1.0), (0.0, 0.0)]]),"Imposible")
    def test_matrizHermitian(self):
        a=Calculadora()
        self.assertEqual(a.matrizHermitian([[(5.0, 0.0), (4.0, 5.0), (6.0, -16.0)], [(4.0, -5.0), (13.0, 0.0), (7.0, 0.0)], [(6.0, 16.0), (7.0, 0.0), (-2.1, 0.0)]]),True)
    def test_matrizHermitianNoes(self):
        a=Calculadora()
        self.assertEqual(a.matrizHermitian([[(5.0, 0.0), (4.0, 5.0)], [(4.0, -5.0), (13.0, 5.4)]]),False)
    def test_matrizHermitianImposible(self):
        a=Calculadora()
        self.assertEqual(a.matrizHermitian([[(5.0, 0.0), (4.0, 5.0), (6.0, -16.0)], [(4.0, -5.0), (13.0, 0.0), (7.0, 0.0)], [(6.0, 16.0), (7.0, 0.0), (-2.1, 0.0)],[(6.0, 16.0), (7.0, 0.0), (-2.1, 0.0)]]),"Imposible")
    def test_productoTensor(self):
        a=Calculadora()
        self.assertEqual(a.productoTensor([[(3.0, 2.0), (5.0, -1.0), (0.0, 2.0)], [(0.0, 0.0), (12.0, 0.0), (6.0, -3.0)], [(2.0, 0.0), (4.0, 4.0), (9.0, 3.0)]],[[(1.0, 0.0), (3.0, 4.0), (5.0, -7.0)], [(10.0, 2.0), (6.0, 0.0), (2.0, 5.0)], [(0.0, 0.0), (1.0, 0.0), (2.0, 9.0)]]),[[(3.0, 2.0), (1.0, 18.0), (29.0, -11.0), (5.0, -1.0), (19.0, 17.0), (18.0, -40.0), (0.0, 2.0), (-8.0, 6.0), (14.0, 10.0)], [(26.0, 26.0), (18.0, 12.0), (-4.0, 19.0), (52.0, 0.0), (30.0, -6.0), (15.0, 23.0), (-4.0, 20.0), (0.0, 12.0), (-10.0, 4.0)], [(0.0, 0.0), (3.0, 2.0), (-12.0, 31.0), (0.0, 0.0), (5.0, -1.0), (19.0, 43.0), (0.0, 0.0), (0.0, 2.0), (-18.0, 4.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (36.0, 48.0), (60.0, -84.0), (6.0, -3.0), (30.0, 15.0), (9.0, -57.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (120.0, 24.0), (72.0, 0.0), (24.0, 60.0), (66.0, -18.0), (36.0, -18.0), (27.0, 24.0)], [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (12.0, 0.0), (24.0, 108.0), (0.0, 0.0), (6.0, -3.0), (39.0, 48.0)], [(2.0, 0.0), (6.0, 8.0), (10.0, -14.0), (4.0, 4.0), (-4.0, 28.0), (48.0, -8.0), (9.0, 3.0), (15.0, 45.0), (66.0, -48.0)], [(20.0, 4.0), (12.0, 0.0), (4.0, 10.0), (32.0, 48.0), (24.0, 24.0), (-12.0, 28.0), (84.0, 48.0), (54.0, 18.0), (3.0, 51.0)], [(0.0, 0.0), (2.0, 0.0), (4.0, 18.0), (0.0, 0.0), (4.0, 4.0), (-28.0, 44.0), (0.0, 0.0), (9.0, 3.0), (-9.0, 87.0)]])
if __name__ == "__main__":
    unittest.main()
	
	
