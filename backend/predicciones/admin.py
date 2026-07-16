from django.contrib import admin
from .models import PrediccionMateria


@admin.register(PrediccionMateria)
class PrediccionMateriaAdmin(admin.ModelAdmin):
    list_display = (
        'alumno',
        'materia',
        'parcial_1',
        'parcial_2',
        'calificacion_tercer_parcial_estimada',
        'riesgo_academico',
        'fecha_prediccion',
    )

    search_fields = (
        'alumno__alumno_id',
        'alumno__nombre',
        'alumno__apellidos',
        'materia__nombre_materia',
    )

    list_filter = (
        'riesgo_academico',
        'materia__grado',
        'materia__area_materia',
        'fecha_prediccion',
    )

    readonly_fields = (
        'fecha_prediccion',
    )