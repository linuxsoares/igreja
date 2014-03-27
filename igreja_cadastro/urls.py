from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'igreja_cadastro.core.views.homepage', name='homepage'),
    url(r'institucional/$', 'igreja_cadastro.core.views.institucional', name='institucional'),
    url(r'campanha/$', 'igreja_cadastro.core.views.campanha', name='campanha'),
    url(r'cadastro/$', 'igreja_cadastro.cadastro_fieis.views.cadastro',  name='cadastro'),
    url(r'cadastro/(\d+)/$', 'igreja_cadastro.cadastro_fieis.views.detail', name='detail' ),
    url(r'images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'igreja_cadastro.views.home', name='home'),
    # url(r'^igreja_cadastro/', include('igreja_cadastro.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)

urlpatterns += staticfiles_urlpatterns()