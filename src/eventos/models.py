from django.db import models
from django.contrib.auth.models import User

ACCION_OFERTA = (
    (0, 'Publicar'),
    (1, 'Aspirar'),
    (2, 'Abandonar'),
    (3, 'Aplicar')
)

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True)

class Evento(models.Model):
    usuario = models.ForeignKey(User)
    tipo = models.ForeignKey(TipoEvento)
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=255)

class Entrevista(models.Model):
    url_video = models.URLField()
    evento = models.ForeignKey(Evento)
    responsable = models.ForeignKey(User)

class Prueba(models.Model):

    ESTADO_PRUEBA = (
        (0, 'En Progreso'),
        (1, 'Finalizado'),
    )

    repositorio = models.URLField()
    estado = models.IntegerField(choices=ESTADO_PRUEBA)
    evento_inicio = models.ForeignKey(Evento, related_name='inicio_prueba')
    evento_fin = models.ForeignKey(Evento, related_name='fin_prueba')
    responsable = models.ForeignKey(User)

class RelacionOferta(models.Model):
    oferta = models.ForeignKey(Oferta)
    accion = models.IntegerField(choices=ACCION_OFERTA)
    evento = models.ForeignKey(Evento)
