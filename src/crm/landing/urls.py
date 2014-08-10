from django.conf.urls import patterns, url


urlpatterns = patterns('crm.landing.views',
                       url(r'^$', 'home', name='landing'),
                       url(r'^faq$', 'faq', name='faq'),
                       url(r'^mail/contact_me/$', 'contact_me', name='contact_me'),
)
