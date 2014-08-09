from django.test import TestCase
from core.models import *

# Create your tests here.

class OfertaTest(TestCase):
    def insertar(self):
        Oferta.objects.create(empresa="codetag", salario=134780, funciones="nada", beneficios="ninguno")
        Oferta.objects.create(empresa="juanito", salario=2342341234, funciones="todo", beneficios="eps y otros")
    
    def test_oferta(self):
        self.insertar()
        oferta1 = Oferta.objects.get(empresa="codetag")
        self.assertEqual(oferta1.empresa, "codetag")

    def test_todos(self):
        Oferta.objects.create(empresa="juanito", salario=12.500, funciones="no hace nada", beneficios="ninguno", tecnologias="java")
        oferta2 = Oferta.objects.get(oferta="juanito")
        self.assertEqual(oferta2.salario, 12.500)
        self.assertEqual(oferta2.empresa,"juanito")
        self.assertEqual(oferta2.funciones,"no hace nada")
        self.assertEqual(oferta2.beneficios,"ninguno")
        self.assertEqual(oferta2.tecnologias,"java")

# Create your tests here.
