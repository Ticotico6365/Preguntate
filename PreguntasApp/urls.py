from django.urls import path

from PreguntasApp.views import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('preguntas/', preguntas, name='preguntas'),
    path('panel_administrador/', panel_administrador, name='panel_administrador'),
    path('login/', do_login, name='login'),
    path('login/out', do_logout, name='logout'),
    path('registro/', registro, name='registro'),
]