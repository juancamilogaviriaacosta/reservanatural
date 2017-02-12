from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuevoUsuario/$', views.nuevo_usuario_vista, name='nuevoUsuario'),
    url(r'^iniciarSesion/$', views.iniciar_sesion_vista, name='iniciarSesion'),
    url(r'^cerrarSesion/$', views.cerrar_sesion_vista, name='cerrarSesion'),
]
