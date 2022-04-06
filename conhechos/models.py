
from django.db import models

class Eje(models.Model):
    eje = models.CharField(max_length=1000, verbose_name="Titulo", blank=True , null= True)
    def __str__(self):
        return self.eje

class Descripcion(models.Model):
    eje = models.ForeignKey(Eje, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='files/')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    def __str__(self):
        return self.titulo

class CumplimosLoPrometidoVideo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.CharField(max_length=1000)
    def __str__(self):
        return self.titulo

class SliderVideo(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=1000)
    def __str__(self):
        return self.titulo