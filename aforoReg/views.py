from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import Place, Camera, Register
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    lugar = Place.objects.get(id=2)
    camara = Camera.objects.get(id=4)
    registro = Register.objects.latest('fecha', 'hora')

    data = {
        'nombre_lugar': lugar.nomlugar,
        'lugar_camara': camara.lugarcam,
        'personas': registro.personas,
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(data)
    else:
        return render(request, 'index.html', data)

# def index(request):
#     lugar = get_object_or_404(Place, id=2)
#     camara = get_object_or_404(Camera, id=4)
#     registro = Register.objects.latest('fecha', 'hora')
#
#     data = {
#         'nombre_lugar': lugar.nomlugar,
#         'lugar_camara': camara.lugarcam,
#         'personas': registro.personas,
#     }
#
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return JsonResponse(data)
#     else:
#         return render(request, 'index.html', data)


def semaforo(request):
    lugar = Place.objects.get(id=5)
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


def info(request):
    return render(request, 'views/info.html')


def prueba(request):
    return render(request, 'views/prueba.html')

