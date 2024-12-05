from django.db import models

# Create your models here.
class Proyect(models.Model):
    titulo = models.CharField(max_length=200)
    rut = models.TextField()
    nombre_apellido = models.TextField()
    URL = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    