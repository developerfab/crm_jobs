# -*- coding: utf-8 -*-

from django.contrib import admin
from core.models import *

class TecnologiaDesarrolladorInline(admin.TabularInline):
    model = TecnologiaDesarrollador

class DesarrolladorAdmin(admin.ModelAdmin):
	inlines = [TecnologiaDesarrolladorInline]

class TecnologiaDesarrolladorInline(admin.TabularInline):
    model = TecnologiaDesarrollador

class OfertaAdmin(admin.ModelAdmin):
	inlines = [TecnologiaDesarrolladorInline]

# Register your models here.
admin.site.register(Oferta, OfertaAdmin)
admin.site.register(Desarrollador, DesarrolladorAdmin)
admin.site.register(Tecnologia)

