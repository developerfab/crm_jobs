# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from core.views import *
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^', include('crm.landing.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ofertas/', include('core.urls')),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html' } , name='crm_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='crm_logout'),
)