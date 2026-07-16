from django.contrib import admin

from .models import PrediccionMateria


@admin.register(PrediccionMateria)
class PrediccionMateriaAdmin(admin.ModelAdmin):
    list_display = (
        'alumno',
        'materia',
        'parcial_1',
        'parcial_2',
        'calificacion_media_tercer_parcial',
        'calificacion_final_media',
        'riesgo_academico',
        'fecha_prediccion',
    )

    list_filter = (
        'riesgo_academico',
        'materia',
        'fecha_prediccion',
    )

    search_fields = (
        'alumno__nombre',
        'alumno__apellido_paterno',
        'materia__nombre',
    )

    readonly_fields = (
        'calificacion_minima_tercer_parcial',
        'calificacion_media_tercer_parcial',
        'calificacion_maxima_tercer_parcial',
        'calificacion_final_minima',
        'calificacion_final_media',
        'calificacion_final_maxima',
        'riesgo_academico',
        'fecha_prediccion',
    )