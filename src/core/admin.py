# -*- coding: utf-8 -*-

from django.contrib import admin
from core.models import *

class TecnologiaDesarrolladorInline(admin.TabularInline):
    model = TecnologiaDesarrollador

class DesarrolladorAdmin(admin.ModelAdmin):
	inlines = [TecnologiaDesarrolladorInline]

class TecnologiaOfertaInline(admin.TabularInline):
    model = TecnologiaOferta

class OfertaAdmin(admin.ModelAdmin):
	inlines = [TecnologiaOfertaInline]

# Register your models here.
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Desarrollador, DesarrolladorAdmin)
admin.site.register(Tecnologia)

