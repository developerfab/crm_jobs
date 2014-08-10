# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Desarrollador(models.Model):
    user = models.OneToOneField(User) 
    telefono = models.CharField(max_length=13)
    tecnologias = models.TextField()
    perfil_github = models.URLField()
    perfil_linkedin = models.URLField()
    perfil_bitbucked = models.URLField()
    perfil_twitter = models.URLField()


    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name_plural = "Desarrolladores"


class Oferta (models.Model):
    empresa = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=12, decimal_places=2)
    funciones = models.TextField()
    beneficios = models.TextField()
    tecnologias = models.TextField()
    estado = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    tags = TaggableManager()
    aplicantes = models.ManyToManyField(Desarrollador)

    class Meta:
        verbose_name_plural = "Ofertas"

    def __unicode__(self):
        return u"%s -  $%s" % (self.empresa, str(self.salario))
