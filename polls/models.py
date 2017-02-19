from __future__ import unicode_literals

from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.db import models
from django import forms


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)


class Especie(models.Model):
    clasificaciontaxonomica = models.CharField(max_length=50, blank=True, null=True)
    descripcionlarga = models.CharField(max_length=255, blank=True, null=True)
    nombrecientifico = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(upload_to='images', null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, null=True)


class Comentario(models.Model):
    texto = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    especie = models.ForeignKey(Especie, null=True)


# Modelo de perfil de usuario que extiende al usuario de Django
class UserProfile(models.Model):
    # Referencia al usuario de Django
    user = models.OneToOneField(User)
    # Atributos extra
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    pais = models.CharField(max_length=50, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    intereses = models.CharField(max_length=200, null=False)


def validar_usuario(self):
    # Verificar que no exista el usuario
    usuario = self.cleaned_data['usuario']
    if User.objects.filter(usuario=usuario):
        raise forms.ValidationError('Usuario ya registrado')
    return usuario


def validar_correo(self):
    # Verificar que no exista el correo
    correo = self.cleaned_data['correo']
    if User.objects.filter(correo=correo):
        raise forms.ValidationError('Correo ya registrado')
    return correo


def validar_password(self):
    # Verificar que el password sea igual al password2
    password = self.cleaned_data['password']
    password2 = self.cleaned_data['password2']
    if password != password2:
        raise forms.ValidationError('Los password no coinciden')
    return password2

# class Detalleespecie(models.Model):
#    clasificaciontaxonomica = models.CharField(max_length=255, blank=True, null=True)
#    descripcionlarga = models.CharField(max_length=255, blank=True, null=True)
#    nombrecientifico = models.CharField(max_length=255, blank=True, null=True)
#    especie = models.ForeignKey('Especie', models.DO_NOTHING, blank=True, null=True)

# class DetalleespecieCategoria(models.Model):
#    detalleespecie = models.ForeignKey(Detalleespecie, models.DO_NOTHING)
#    categorias = models.ForeignKey(Categoria, models.DO_NOTHING)

# class EspecieComentario(models.Model):
#    especie = models.ForeignKey(Especie, models.DO_NOTHING)
#    comentarios = models.ForeignKey(Comentario, models.DO_NOTHING)
