from unittest import TestCase
from codigo_avulso_test_tutorial.figura_geometrica import FiguraGeometrica 

class TestFiguraGeometrica(TestCase):
	def setUp(self):
		TestCase.setUp(self)
		self.fig = FiguraGeometrica()
	def test_get_area(self):
		self.assertRaises(NotImplementedError, self.fig.get_area)
	def test_get_perimetro(self):
		self.assertRaises(NotImplementedError, self.fig.get_perimetro)
