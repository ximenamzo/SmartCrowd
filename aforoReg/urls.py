from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('semaforo/', views.semaforo, name='semaforo'),
    path('info/', views.info, name='info'),
    path('prueba/', views.prueba, name='prueba'),
]