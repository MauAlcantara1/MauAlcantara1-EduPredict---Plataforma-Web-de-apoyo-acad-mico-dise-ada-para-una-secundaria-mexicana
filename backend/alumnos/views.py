from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm


def lista_alumnos(request):
    alumnos = Alumno.objects.all().order_by('grado', 'grupo', 'apellidos')

    contexto = {
        'alumnos': alumnos
    }

    return render(request, 'alumnos/lista_alumnos.html', contexto)

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
        
    else:
        form = AlumnoForm()

    contexto = {
        'form': form
    }

    return render(request, 'alumnos/crear_alumno.html', contexto)
    
