from django.conf import settings
from django.conf.urls import patterns, include
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from macrosurl import url


urlpatterns = patterns('',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', 'articulos.views.inicio', name='inicio'),
    url(r'^articulos/:articulo_id/', 'articulos.views.ver_articulo', name='ver_articulo'),
    url(r'^categorias/:categoria_slug/', 'articulos.views.view_category', name='view_category'),
    url(r'^busqueda/$', 'articulos.views.buscar', name='buscar'),
    url(r'^publicar/$', 'articulos.views.publicar', name='publicar'),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
