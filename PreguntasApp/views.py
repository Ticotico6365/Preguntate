import random
from datetime import datetime
from PreguntasApp import preguntas as pre
from django.shortcuts import render

from PreguntasApp.models import Pregunta


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def preguntas(request):

    empezar = False
    pregunta = ""
    if request.method == 'POST':
        empezar = True
        if request.POST.get('empezar'):
            pre.empezar()
        elif request.POST.get('pregunta'):
            pregunta = pre.extraer_pregunta()
        elif request.POST.get('terminar'):
            empezar = False
            pre.reiniciar()



    return render(request, 'preguntas.html', {'empezar': empezar, 'pregunta': pregunta, 'preguntas_respondidas':pre.preguntas_respondiodias})