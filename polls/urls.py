from django.conf.urls import url
from django.contrib.contenttypes import views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuevoUsuario/$', views.nuevo_usuario_vista, name='nuevoUsuario'),
    url(r'^iniciarSesion/$', views.iniciar_sesion_vista, name='iniciarSesion'),
    url(r'^cerrarSesion/$', views.cerrar_sesion_vista, name='cerrarSesion'),
    url(r'^modificarUsuario/$', views.modificar_usuario_vista, name='modificarUsuario'),
    url(r'^verEspecie/(?P<id_especie>\d+)/$', views.detallar_especie_vista, name='verEspecie'),
    url(r'^nuevoComentario/$', views.nuevo_comentario, name='nuevoComentario'),
]
