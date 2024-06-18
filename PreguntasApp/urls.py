from django.urls import path

from PreguntasApp.views import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('preguntas/', preguntas, name='preguntas'),
]