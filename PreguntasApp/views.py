from PreguntasApp import preguntas as pre
from django.shortcuts import render, redirect

from PreguntasApp.models import *
from django.contrib.auth import authenticate, login, logout


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
        username = request.POST.get('nickname')
        password = request.POST.get('contrasena')


        if not Usuario.objects.filter(username=username).exists():
            errors["username"] = "Nombre de usuario Incorrecto"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirección tras un login exitoso
                return redirect('inicio')
            else:
                errors['contrasena'] = "contraseña incorrecta"
                # Mensaje de error si la autenticación falla
                return render(request, 'login.html', {"error": errors})

    # Mostrar formulario de login para método GET
    return render(request, 'login.html', {"error": errors})

def do_logout(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html')
    else:
        nickname = request.POST.get('nickname')
        password = request.POST.get('contrasena')
        email = request.POST.get('e_mail')

        if nickname == '' or password == '' or email == '':
            return render(request, 'registro.html', {'error': 'Todos los campos son obligatorios'})

        if Usuario.objects.filter(email=email).exists():
            return render(request, 'registro.html', {'error': 'El usuario ya existe'})
        else:
            user = Usuario(username=nickname, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')