from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

class Especie(models.Model):
    clasificaciontaxonomica = models.CharField(max_length=50, blank=True, null=True)
    descripcionlarga = models.CharField(max_length=255, blank=True, null=True)
    nombrecientifico = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    foto = models.ImageField(upload_to='images/', null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, null=True)

class Comentario(models.Model):
    texto = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=30, blank=True, null=True)
    especie = models.ForeignKey(Especie, null=True)

#class UsuarioForm(ModelForm):
#    nombres = form.CharField(max_length=60 null=False)
#    apellidos = form.CharField(max_length=60, null=False)
#    pais = form.CharField(max_length=30, null = False)
#    ciudad = form.CharField(max_length=40, null=False)
#    correo = form.CharField(max_length=30, null = False)
#    intereses = form.CharField(max_length=255, null=False)


#class Detalleespecie(models.Model):
#    clasificaciontaxonomica = models.CharField(max_length=255, blank=True, null=True)
#    descripcionlarga = models.CharField(max_length=255, blank=True, null=True)
#    nombrecientifico = models.CharField(max_length=255, blank=True, null=True)
#    especie = models.ForeignKey('Especie', models.DO_NOTHING, blank=True, null=True)

#class DetalleespecieCategoria(models.Model):
#    detalleespecie = models.ForeignKey(Detalleespecie, models.DO_NOTHING)
#    categorias = models.ForeignKey(Categoria, models.DO_NOTHING)

#class EspecieComentario(models.Model):
#    especie = models.ForeignKey(Especie, models.DO_NOTHING)
#    comentarios = models.ForeignKey(Comentario, models.DO_NOTHING)