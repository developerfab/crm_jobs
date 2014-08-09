from django.test import TestCase
from core.models import *

# Create your tests here.

class OfertaTest(TestCase):
    def insertar(self):
        Oferta.objects.create(empresa="codetag", salario=134780, funciones="nada", beneficios="ninguno")
        Oferta.objects.create(empresa="juanito", salario=2342341234, funciones="todo", beneficios="eps y otros")
    
    def test_oferta(self):
        self.insertar()
        empresa1 = Oferta.objects.get(empresa="codetag")
        empresa2 = Oferta.objects.get(empresa="juanito")
        self.assertEqual(empresa1.empresa, "codetag")

# Create your tests here.
