# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from core.models import *
from django.db.models import Q
import operator


def buscar_ofertas(request):
    try:
        busqueda = request.POST['palabras'].replace(" ", "").split(",")
        ofertas = Oferta.objects.filter(reduce(operator.or_, ((Q(tecnologias__contains=x) | Q(funciones__contains=x) | Q(empresa__contains=x)) for x in busqueda)))

    except Exception, e:
        print e
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
