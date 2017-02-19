from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }
        help_texts = {
            'username': 'Este será el código de usuario para iniciar sesión'
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nombres', 'apellidos', 'pais', 'ciudad', 'intereses')
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'pais': 'País',
            'ciudad': 'Ciudad',
            'intereses': 'Intereses'
        }

