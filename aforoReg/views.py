from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import Place, Camera, Register
from django.http import JsonResponse, HttpRequest

# Create your views here.
def index(request):
    lugares = Place.objects.order_by('fec_cre')
    return render(request, 'index.html', {'lugares': lugares})


def semaforo(request):
    lugar = Place.objects.get(id=8)
    camara = Camera.objects.get(id=4)
    registro = Register.objects.latest('fecha', 'hora')

    data = {
        'nombre_lugar': lugar.nomlugar,
        'lugar_camara': camara.lugarcam,
        'personas': registro.personas,
    }

    # if request.is_ajax:
    #     return JsonResponse(diccionario)
    # 
    # return render(request, 'views/semaforo.html', diccionario)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(data)
    else:
        return render(request, 'views/semaforo.html', data)


def sobre_nosotros(request):
    return render(request, 'views/sobre-nosotros.html')

