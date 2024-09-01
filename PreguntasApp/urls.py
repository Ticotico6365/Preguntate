from django.urls import path

from PreguntasApp.views import *

urlpatterns = [
    path('inicio/', preguntas, name='inicio'), #la página principal es directamente el juego y si estas logeado puedes hacer el resto
    path('login/', do_login, name='login'),
    path('login/out', do_logout, name='logout'),
    path('registro/', registro, name='registro'),
    path('panel_administrador/', panel_administrador, name='panel_administrador'),
    path('panel_usuario/', panel_usuario, name='panel_usuario'),
    path('panel_usuario/preguntas_privadas', panel_usuario_priv, name='panel_usuario_privado'),
    path('panel_usuario/preguntas_publicas', panel_usuario_publi, name='panel_usuario_publico'),
    path('panel_usuario/privatizar/<int:id>/', hacer_priv, name='hacer_privada'), #Tengo que ver como lo hago (tipo carrito)
    path('panel_usuario/borrar/<int:id>/', borrar, name='borrar_pregunta'),

]