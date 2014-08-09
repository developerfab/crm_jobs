from django.db import models

# Create your models here.

class Oferta (models.Model):
	empresa = models.CharField(max_length=100)
	salario = models.DecimalField(max_digits=12, decimal_places=2)
	funciones = models.TextField()
	beneficios = models.TextField()

	class Meta:
		verbose_name_plural = "Ofertas"

	def __unicode__ (self):
		return u"%s -  %s" % (empresa, str(salario))

