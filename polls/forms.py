from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Comentario


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electronico',
        }
        help_texts = {
            'username': 'Este sera el codigo de usuario para iniciar sesion'
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('foto', 'nombres', 'apellidos', 'pais', 'ciudad', 'intereses')
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'foto': 'Foto',
            'pais': 'Pais',
            'ciudad': 'Ciudad',
            'intereses': 'Intereses'
        }

class ComentarioForm(forms.ModelForm):
    texto = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comentario
        fields = ('correo', 'texto')
        labels = {
            'correo': 'Correo electronico',
            'texto': 'Comentario'
        }
        widgets = {
            'texto': forms.Textarea
        }