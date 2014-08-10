# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from core.models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import operator


#Esta funcion se encarga de buscar las ofertas que se reciben a traves del request
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
    return render(request, 'lista_ofertas.html', {"ofertas": ofertas, 'origen': "Resultados de la busqueda"})


#Esta funcion se encarga de enviar la oferta seleccionada de manera individual
def ver_oferta(request):
    try:
        identificador = request.GET['id']
        oferta = Oferta.objects.get(id=identificador)
        ofertas_similares = Oferta.objects.get(id=identificador).tags.similar_objects()
    except:
        oferta = None
    return render(request, 'oferta.html', {"oferta": oferta, "similares": ofertas_similares})

@login_required(login_url="/login/")
def vincular_oferta(request):
    usuario = request.user.id
    oferta = request.POST['id_oferta']
    print(usuario)
    print(oferta)

#login 
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            render(request, 'home.html')
        else:
            render(request, 'home.html')
    else:
        render(request, 'home.html')
