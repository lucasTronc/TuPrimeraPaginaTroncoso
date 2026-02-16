from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)