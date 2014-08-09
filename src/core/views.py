# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from core.models import *


# Create your views here.
def buscar_ofertas(request):
    try:
        busqueda = request.POST['palabras']
        ofertas = Oferta.objects.all().filter(tecnologia__contains=busqueda)
    except:
        ofertas = Oferta.objects.all()  

    paginator = Paginator(ofertas, 25) 
    try:
        pagina = request.GET.get('page')
    except:
        pagina = 1
    try:
        ofertas = paginator.page(pagina)
    except:
        ofertas = paginator.page(1)

    return render(request, 'lista_ofertas.html', {"ofertas": ofertas})
