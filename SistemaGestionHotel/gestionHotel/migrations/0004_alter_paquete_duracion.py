# Generated by Django 5.0.6 on 2024-06-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionHotel', '0003_alter_servicio_tarifa_paquete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='duracion',
            field=models.DurationField(help_text='Duracion del paquete', verbose_name='Duracion'),
        ),
    ]