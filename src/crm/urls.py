# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from core.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^', include('crm.landing.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ofertas/', include('core.urls')),

)
