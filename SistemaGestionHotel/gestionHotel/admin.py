from django.contrib import admin

from gestionHotel.models import *

admin.site.register(Hotel)
admin.site.register(Servicio)
admin.site.register(Paquete)
admin.site.register(Habitacion)
admin.site.register(ReservaHabitacion)
admin.site.register(Pago)