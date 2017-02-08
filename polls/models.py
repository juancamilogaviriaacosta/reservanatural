from __future__ import unicode_literals
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)


class Comentario(models.Model):
    texto = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)


class Detalleespecie(models.Model):
    clasificaciontaxonomica = models.CharField(max_length=255, blank=True, null=True)
    descripcionlarga = models.CharField(max_length=255, blank=True, null=True)
    nombrecientifico = models.CharField(max_length=255, blank=True, null=True)
    especie = models.ForeignKey('Especie', models.DO_NOTHING, blank=True, null=True)


class DetalleespecieCategoria(models.Model):
    detalleespecie = models.ForeignKey(Detalleespecie, models.DO_NOTHING)
    categorias = models.ForeignKey(Categoria, models.DO_NOTHING)


class Especie(models.Model):
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

class EspecieComentario(models.Model):
    especie = models.ForeignKey(Especie, models.DO_NOTHING)
    comentarios = models.ForeignKey(Comentario, models.DO_NOTHING)