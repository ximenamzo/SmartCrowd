from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .models import Place, Camera, Register

# Create your views here.
def index(request):
    lugares = Place.objects.order_by('fec_cre')
    return render(request, 'index.html', {'lugares': lugares})

