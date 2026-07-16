from django.contrib import admin
from .models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'alumno_id',
        'nombre',
        'apellidos',
        'grado',
        'grupo',
        'turno',
        'edad',
        'sexo',
        'fecha_registro',
    )

    search_fields = (
        'alumno_id',
        'nombre',
        'apellidos',
    )

    list_filter = (
        'grado',
        'grupo',
        'turno',
        'sexo',
    )