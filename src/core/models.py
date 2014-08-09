# -*- coding: utf-8 -*-
from django.db import models


class Oferta (models.Model):
    empresa = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=12, decimal_places=2)
    funciones = models.TextField()
    beneficios = models.TextField()
    tecnologias = models.TextField()
    estado = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name_plural = "Ofertas"

    def __unicode__(self):
        return u"%s -  $%s" % (self.empresa, str(self.salario))
