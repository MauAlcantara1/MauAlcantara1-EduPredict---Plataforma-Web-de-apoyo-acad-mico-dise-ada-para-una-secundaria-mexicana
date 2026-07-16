from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('nuevo/', views.crear_alumno, name='crear_alumno'),
]