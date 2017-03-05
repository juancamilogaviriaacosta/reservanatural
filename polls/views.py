from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Especie, UserProfile, Comentario, Categoria
from .forms import UserForm, UserProfileForm, ComentarioForm



# Create your views here.
def index(request):
    lista_categorias = Categoria.objects.all()
    if request.method == 'POST':
        lista_especies = Especie.objects.filter(categoria_id = request.POST.get('categorias_combo'))
    else:
        lista_especies = Especie.objects.all()
    context = {'lista_especies': lista_especies, 'lista_categorias': lista_categorias}
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

    # No haga nada si el metodo es get para que se vean los datos previos
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        # Traer los nuevos datos del request, con la instancia que se va a actualizar
        profile_form = UserProfileForm(request.POST, request.FILES, instance=perfilModificable)

        # Asignar la referencia al usuario Django desde el perfil
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
    # Carga la referencia a la especie
    ref_especie = Especie.objects.get(id=id_especie)

    # Carga el correo del usuario actual
    if request.user.is_authenticated:
        correo_usr = request.user.email
        form = ComentarioForm(initial={'correo': correo_usr})
    else:
        form = ComentarioForm()

    # Cargar el listado de comentarios de la especie
    lista_comentarios = Comentario.objects.filter(especie_id=id_especie)
    # Cargar la especie actual
    especie = Especie.objects.get(id=id_especie)

    # Define el contexto para el template
    context = {
        'especie': especie,
        'lista_comentarios': lista_comentarios,
        'formComentario': form,
    }

    if request.method == 'GET':
        return render(request, 'polls/detalleEspecie.html', context)

    if request.method == 'POST':
        # Llena el form con los datos introducidos por el usuario
        form = ComentarioForm(data=request.POST)
        # Carga la referencia a la especie
        form.instance.especie = ref_especie

        if form.is_valid():
            # Guardar el comentario
            form.save()

    return HttpResponseRedirect('/verEspecie/%s' % id_especie)

