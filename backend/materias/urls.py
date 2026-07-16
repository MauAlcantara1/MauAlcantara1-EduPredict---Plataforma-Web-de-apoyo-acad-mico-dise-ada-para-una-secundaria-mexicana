from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_materias, name='lista_materias'),
    path('por-alumno/<int:alumno_id>/', views.materias_por_alumno, name='materias_por_alumno'),
]