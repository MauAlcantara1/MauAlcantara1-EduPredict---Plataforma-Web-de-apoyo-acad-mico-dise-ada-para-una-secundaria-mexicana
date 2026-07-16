from django.shortcuts import render
from .models import Materia
from django.http import JsonResponse
from alumnos.models import Alumno


def lista_materias(request):
    materias = Materia.objects.all().order_by(
        'grado',
        'area_materia',
        'nombre_materia'
    )

    contexto = {
        'materias': materias
    }

    return render(request, 'materias/lista_materias.html', contexto)

def materias_por_alumno(request, alumno_id):
    try:
        alumno = Alumno.objects.get(id=alumno_id)

        materias = Materia.objects.filter(
            grado=alumno.grado
        ).order_by('nombre_materia')

        datos=[]

        for materia in materias:
            datos.append({
                'id': materia.id,
                'nombre': materia.nombre_materia,
            })

        return JsonResponse({
            'materias': datos
        })
    
    except Alumno.DoesNotExist:
        return JsonResponse({
            'materias': []
        })