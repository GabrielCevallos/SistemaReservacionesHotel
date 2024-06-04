from django.db import models
from datetime import datetime, time, timedelta


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


start_time = time(0, 0, 0)
end_time = time(23, 59, 59)

today = datetime.today()
start_datetime = datetime.combine(today, start_time)
end_datetime = datetime.combine(today, end_time)

duration = end_datetime - start_datetime


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


class EstadoHabitacion(models.Choices):
    DISPONIBLE = 'Disponible'
    OCUPADA = 'Ocupada'
    RESERVADA = 'Reservada'


class Habitacion(models.Model):
    numeroHabitacion = models.PositiveIntegerField()
    numeroCamas = models.PositiveIntegerField()
    numeroBaños = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)
    capacidadPersonas = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel,
                              on_delete=models.CASCADE,
                              related_name='habitacion_list')
    estado = models.CharField(max_length=15,
                              choices=EstadoHabitacion.choices,
                              default=EstadoHabitacion.DISPONIBLE)

    def __str__(self):
        return f'{self.numeroHabitacion} - {self.hotel.nombre}'

class ReservaHabitacion(models.Model):
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    cantidadPersonas = models.PositiveIntegerField()
    habitacion = models.ForeignKey(Habitacion,
                                   on_delete=models.CASCADE,
                                   related_name='reserva_list')
    paquete = models.ForeignKey(Paquete,
                                on_delete=models.CASCADE,
                                related_name='reserva_list')

    def __str__(self):
        return f'{self.habitacion.numeroHabitacion} - {self.habitacion.hotel.nombre}'

class Pago(models.Model):
    fecha = models.DateField()
    metodoPago = models.CharField(max_length=50)
    monto = models.PositiveIntegerField()
    reserva = models.ForeignKey(ReservaHabitacion,
                                on_delete=models.CASCADE,
                                related_name='pago_list')

    def __str__(self):
        return f'{self.monto} - {self.reserva.habitacion.numeroHabitacion}'