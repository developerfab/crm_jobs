from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', buscar_ofertas, name="buscar_ofertas"),
    url(r'^visualizar/$', ver_oferta, name="ver_oferta"),
    url(r'^similares/$', buscar_ofertas_similares, name="buscar_ofertas_similares"),
)
