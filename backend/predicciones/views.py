from django.shortcuts import render, redirect
from .models import PrediccionMateria
from .forms import PrediccionMateriaForm
from django.shortcuts import render, redirect, get_object_or_404


def lista_predicciones(request):

    predicciones = PrediccionMateria.objects.select_related(
        'alumno',
        'materia'
    ).all().order_by('-fecha_prediccion')

    contexto = {
        'predicciones': predicciones
    }

    return render(request, 'predicciones/lista_predicciones.html', contexto)

def crear_prediccion(request):
    if request.method == 'POST':
        form = PrediccionMateriaForm(request.POST)

        if form.is_valid():
            prediccion = form.save()
            return redirect('detalle_prediccion', prediccion_id=prediccion.id)
    else:
        form = PrediccionMateriaForm()

    contexto = {
        'form': form
    }

    return render(request, 'predicciones/crear_prediccion.html', contexto)

def detalle_prediccion(request, prediccion_id):
    prediccion = get_object_or_404(
        PrediccionMateria.objects.select_related('alumno', 'materia'),
        id=prediccion_id
    )

    contexto = {
        'prediccion': prediccion
    }

    return render(request, 'predicciones/detalle_prediccion.html', contexto)