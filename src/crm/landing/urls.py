from django.conf.urls import patterns, include, url


urlpatterns = patterns('crm.landing.views',
    # Examples:
    # url(r'^$', 'crm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'home', name='landing'),
    url(r'^faq$', 'faq', name='faq'),
)
