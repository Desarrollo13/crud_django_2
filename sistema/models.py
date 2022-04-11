from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100,verbose_name='Título')
    imagen = models.ImageField(upload_to="imagenes/",verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name='Descripcíon',null=True)
    def __str__(self) -> str:
     fila="Titulo: " + self.titulo + " - " "Descripcíon: " + self.descripcion
     return fila