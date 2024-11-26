
# Create your models here.
from django.db import models

class Carpeta(models.Model):
    titulo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.titulo

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_limite = models.DateField()
    
    def __str__(self):
        return self.titulo

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_limite = models.DateField()
    
    def __str__(self):
        return self.titulo
