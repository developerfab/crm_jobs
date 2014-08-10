# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
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


class Desarrollador(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='Correo',
        max_length=255,
        unique=True,
    )

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=13)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    tecnologias = models.ManyToManyField(Tecnologia, through= 'TecnologiaDesarrollador')

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name_plural = "Desarrolladores"
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


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
    nivel = models.IntegerField(choices=NIVELES_DESARROLLADOR)
    oferta = models.ForeignKey(Oferta)

class TecnologiaDesarrollador(models.Model):
    desarrollador = models.ForeignKey(Desarrollador)
    tecnologia  = models.ForeignKey(Tecnologia)
    nivel = models.IntegerField(choices=NIVELES_DESARROLLADOR)
    