from PreguntasApp import preguntas as pre
from django.shortcuts import render, redirect

from PreguntasApp.models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def panel_administrador(request):
    return render(request, 'panel_administrador.html')

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

def do_login(request):
    errors = {}
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')


        if not Usuario.objects.filter(nickname=nickname).exists():
            errors["nickname"] = "Usuario Incorrecto"
        else:
            user = authenticate(request, nickname=nickname, password=password)
            if user is not None:
                login(request, user)
                # Redirección tras un login exitoso
                return redirect('inicio')
            else:
                errors['contraseña'] = "contraseña incorrecta"
                # Mensaje de error si la autenticación falla
                return render(request, 'login.html', {"error": errors})

    # Mostrar formulario de login para método GET
    return render(request, 'login.html', {"error": errors})