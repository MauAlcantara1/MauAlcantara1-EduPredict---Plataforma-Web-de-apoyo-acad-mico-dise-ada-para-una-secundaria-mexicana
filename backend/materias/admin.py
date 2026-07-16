from django.contrib import admin
from .models import Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_materia',
        'area_materia',
        'grado',
        'dificultad_materia',
        'horas_clase_semana',
    )

    search_fields = (
        'nombre_materia',
        'area_materia',
    )

    list_filter = (
        'grado',
        'area_materia',
        'dificultad_materia',
    )