from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno

        fields = [
            'alumno_id',
            'nombre',
            'apellidos',
            'grado',
            'grupo',
            'turno',
            'edad',
            'sexo',
        ]

        widgets = {
            'alumno_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: A001'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del alumno'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos del alumno'
            }),
            'grado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'grupo': forms.Select(attrs={
                'class': 'form-control',
            }),
            'turno': forms.Select(attrs={
                'class': 'form-select'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
        }