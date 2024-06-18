import random

from PreguntasApp.models import Pregunta

preguntas = []
preguntas_respondiodias = []

def empezar():
    bbdd_preguntas = Pregunta.objects.all().values_list('pregunta_text', flat=True)
    for pregunta in bbdd_preguntas:
        preguntas.append(pregunta)
    random.shuffle(preguntas)

def extraer_pregunta():
    if len(preguntas) == 0:
        empezar()
    pregunta = preguntas.pop()
    preguntas_respondiodias.append(pregunta)
    return pregunta

def reiniciar():
    preguntas.clear()
    preguntas_respondiodias.clear()