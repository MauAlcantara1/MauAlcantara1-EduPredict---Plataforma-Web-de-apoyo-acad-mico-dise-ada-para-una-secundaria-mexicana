from django.shortcuts import render

from alumnos.models import Alumno
from materias.models import Materia
from predicciones.models import PrediccionMateria


def dashboard(request):
    total_alumnos = Alumno.objects.count()
    total_materias = Materia.objects.count()
    total_predicciones = PrediccionMateria.objects.count()
    riesgo_alto = PrediccionMateria.objects.filter(riesgo_academico='ALTO').count()

    ultimas_predicciones = PrediccionMateria.objects.select_related(
        'alumno',
        'materia'
    ).order_by('-fecha_prediccion')[:5]

    contexto = {
        'total_alumnos': total_alumnos,
        'total_materias': total_materias,
        'total_predicciones': total_predicciones,
        'riesgo_alto': riesgo_alto,
        'ultimas_predicciones': ultimas_predicciones,
    }

    return render(request, 'core/dashboard.html', contexto)