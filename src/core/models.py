# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

NIVELES_DESARROLLADOR = (
        (0, u'Junior'),
        (1, u'Semisenior'),
        (2, u'Senior'),
    )

class Tecnologia (models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s" % (self.nombre)

class Desarrollador(models.Model):
    user = models.OneToOneField(User) 
    telefono = models.CharField(max_length=13)
    perfil_github = models.URLField(blank=True)
    perfil_linkedin = models.URLField(blank=True)
    perfil_bitbucked = models.URLField(blank=True)
    perfil_twitter = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, through= 'TecnologiaDesarrollador')
    
    class Meta:
        verbose_name_plural = "Desarrolladores"

class Oferta (models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=12, decimal_places=2)
    funciones = models.TextField()
    beneficios = models.TextField()
    estado = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    tags = TaggableManager()
    aplicantes = models.ManyToManyField(Desarrollador)
    tecnologias = models.ManyToManyField(Tecnologia, through= 'TecnologiaOferta')

    class Meta:
        verbose_name_plural = "Ofertas"

    def __unicode__(self):
        return u"%s -  $%s" % (self.empresa, str(self.salario))

class TecnologiaOferta(models.Model):
    tecnologia  = models.ForeignKey(Tecnologia)
    oferta = models.ForeignKey(Oferta)
    nivel = models.IntegerField(choices=NIVELES_DESARROLLADOR)

class TecnologiaDesarrollador(models.Model):
    desarrollador = models.ForeignKey(Desarrollador)
    tecnologia  = models.ForeignKey(Tecnologia)
    nivel = models.IntegerField(choices=NIVELES_DESARROLLADOR)
    
