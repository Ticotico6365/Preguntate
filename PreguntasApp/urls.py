from django.urls import path

from PreguntasApp.views import *

urlpatterns = [
    path('inicio/', preguntas, name='inicio'), #la página principal es directamente el juego y si estas logeado puedes hacer el resto
    path('panel_administrador/', panel_administrador, name='panel_administrador'),
    path('login/', do_login, name='login'),
    path('login/out', do_logout, name='logout'),
    path('registro/', registro, name='registro'),
]