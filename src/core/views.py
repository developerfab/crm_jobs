# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render, redirect
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
    tecnologias = Tecnologia.objects.all()
    niveles = NIVELES_DESARROLLADOR

    try:
        busqueda = request.POST['palabras'].replace(" ", "").split(",")
        tecnologia = request.POST['tecnologia']
        nivel = request.POST['nivel']
        print tecnologia
        ofertas = Oferta.objects.filter(reduce(operator.or_, ((Q(funciones__contains=x) | Q(empresa__contains=x)) for x in busqueda)) & Q(tecnologias__nombre=tecnologia))

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

    return render(request, 'lista_ofertas.html', {"ofertas": ofertas, 'origen': "Resultados de la busqueda", 'tecnologias': tecnologias, 'niveles': niveles})


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

#login de usuarios
def login_user(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        print("user: "+username+" pass: "+password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('landing')
            else:
                print("error usuario inactivo")
                return render(request, 'login.html')
        else:
            print("error asdf")
            return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
