from django.db import models
from datetime import timedelta

# Create your models here.
class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    tipoServicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    disponibilidad = models.BooleanField()
    tarifa = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel,
                              on_delete=models.CASCADE,
                              related_name='servicio_list')


    def __str__(self):
        return self.tipoServicio

class Paquete(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.DurationField("Duracion", help_text="Duracion del paquete")
    categoria = models.CharField(max_length=50)
    beneficios = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel,
                              on_delete=models.CASCADE,
                              related_name='paquete_list')
    servicio = models.ManyToManyField(Servicio, related_name='paquete_list')

    def __str__(self):
        return self.nombre

