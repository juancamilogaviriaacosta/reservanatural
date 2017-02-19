from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Especie, UserProfile
from .forms import UserForm, UserProfileForm


# Create your views here.
def index(request):
    lista_especies = Especie.objects.all()
    context = {'lista_especies': lista_especies}

    return render(request, 'polls/index.html', context)


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


def nuevo_usuario_vista(request):
    if request.method == 'POST':
        # Crea los formularios
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Valida que los formularios esten correctos
        if user_form.is_valid() and profile_form.is_valid():

            # Guarda los datos del usuario a DB
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Guarda los datos del perfil del usuario a DB
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Devuelve a la pagina de inicio

            return HttpResponseRedirect(reverse('index'))


        else:
            # Log en consola de los errores presentados
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'formUsuario': user_form,
        'formPerfil': profile_form
    }

    return render(request, 'polls/registro.html', context)


def modificar_usuario_vista(request):
    # Obtiene los datos de los formularios
    usuarioModificable = request.user
    perfilModificable = UserProfile.objects.get(user_id=request.user.id)

    profile_form = UserProfileForm(instance=perfilModificable)
    user_form = UserForm(instance=usuarioModificable)

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        # Traer los nuevos datos del request, con la instancia que se va a actualizar
        profile_form = UserProfileForm(data=request.POST, instance=perfilModificable)

        #Asignar la referencia al usuario Django desde el perfil
        profile_form.instance.user_id = request.user.id

        # Valida que los formularios esten correctos
        if profile_form.is_valid():

            # Guarda los datos  nuevos del perfil del usuario a DB
            profile = profile_form.save(commit=False)
            usr = user_form.save(commit=False)

            usr.save()
            profile.save()

            # Devuelve a la pagina de inicio
            return HttpResponseRedirect(reverse('index'))

        else:
            # Log en consola de los errores presentados
            print(profile_form.errors)

    context = {
        'formPerfil': profile_form
    }

    return render(request, 'polls/actualizarUsuario.html', context)


def detallar_especie_vista(request, id_especie):
    especie = Especie.objects.get(id=id_especie)
    context = {'especie': especie}
    if request.method == 'GET':
        return render(request, 'polls/detalleEspecie.html', context)
