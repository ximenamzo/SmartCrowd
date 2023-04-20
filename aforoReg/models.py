from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone

# Create your models here.
class Place(models.Model):
    nomlugar=models.CharField(max_length=50)
    calle=models.CharField(max_length=50)
    num=models.CharField(max_length=10)
    colonia=models.CharField(max_length=50)
    municipio=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    fec_cre=models.DateTimeField(auto_now_add=True)
    fec_mod=models.DateTimeField(auto_now=True)

class Camera(models.Model):
    id_place=models.IntegerField()
    lugarcam=models.CharField(max_length=50)
    num_cam_lug=models.IntegerField()

class Register(models.Model):
    id_place=models.IntegerField()
    id_cam=models.IntegerField()
    personas=models.IntegerField()
    fecha=models.DateField(default=timezone.now, verbose_name='Fecha', help_text='Fecha en formato Y-M-D')
    hora = models.TimeField(default=timezone.now, verbose_name='Hora', help_text='Hora en formato HH:MM:SS')