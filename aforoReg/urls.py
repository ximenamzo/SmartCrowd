from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('semaforo/', views.semaforo, name='semaforo'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre-nosotros'),
    path('prueba/', views.prueba, name='prueba'),
]