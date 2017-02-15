from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Especie, UsuarioForm, UpdateUsuarioForm


# Create your views here.
def index(request):
    lista_especies = Especie.objects.all()
    context = {'lista_especies': lista_especies}
    return render(request, 'polls/index.html', context)

def detallar_especie_vista(request, id_especie):
    especie = Especie.objects.get(id = id_especie)
    context = {'especie': especie}
    if request.method == 'GET':
        return render(request, 'polls/detalleEspecie.html', context)

def nuevo_usuario_vista(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            usuario = cleaned_data.get('usuario')
            nombres = cleaned_data.get('nombres')
            apellidos = cleaned_data.get('apellidos')
            pais = cleaned_data.get('pais')
            ciudad = cleaned_data.get('ciudad')
            correo = cleaned_data.get('correo')
            intereses = cleaned_data.get('intereses')
            password = cleaned_data.get('password')

            user_model = User.objects.create_user(username=usuario, password=password)
            user_model.nombres = nombres
            user_model.apellidos = apellidos
            user_model.pais = pais
            user_model.ciudad = ciudad
            user_model.correo = correo
            user_model.intereses = intereses

            return HttpResponseRedirect(reverse('index'))

    else:
        form = UsuarioForm()
    context = {
        'form': form
    }
    return render(request, 'polls/registro.html', context)


def iniciar_sesion_vista(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))

    mensaje = ''
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            mensaje = 'Nombre de usuario o clave no valido'

    return render(request, 'polls/inicio_sesion.html', {'mensaje': mensaje})


def cerrar_sesion_vista(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def modificar_usuario_vista(request):
    #Obtiene el usuario que hace el request
    usuarioEditable = request.user


    if request.method == 'POST':
        form = UpdateUsuarioForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            nombres = cleaned_data.get('nombres')
            apellidos = cleaned_data.get('apellidos')
            correo = cleaned_data.get('correo')
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')

            #Obtiene la referencia al usuario
            user_model = User.objects.get(id=usuarioEditable.id)

            #Guarda las nuevas propiedades
            user_model.first_name = nombres
            user_model.last_name = apellidos
            user_model.email = correo


            #Actualiza el password solo si coinciden
            if password == password2:
                user_model.set_password(password)
                # Refresca la sesion por el cambio de password
                update_session_auth_hash(request, user_model)

            #Persiste el usuario a DB
            user_model.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        form = UpdateUsuarioForm()
    context = {
        'form': form
    }
    return render(request, 'polls/actualizarUsuario.html', context)
