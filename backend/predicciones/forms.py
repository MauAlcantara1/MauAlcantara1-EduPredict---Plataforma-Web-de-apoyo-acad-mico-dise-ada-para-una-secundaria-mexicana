from django import forms

from alumnos.models import Alumno
from materias.models import Materia
from .models import PrediccionMateria


class PrediccionMateriaForm(forms.ModelForm):
    class Meta:
        model = PrediccionMateria

        fields = [
            'alumno',
            'materia',
            'horas_clase_semana',
            'promedio_general_anterior',
            'materias_reprobadas_previas',
            'promedio_materia_anterior',
            'parcial_1',
            'parcial_2',
            'promedio_tareas',
            'porcentaje_tareas_entregadas',
            'participacion',
            'conducta',
            'faltas_materia',
            'retardos_materia',
            'asistencia_porcentaje',
            'horas_estudio_semana_materia',
            'apoyo_familiar_nivel',
            'acceso_internet',
            'trabaja',
            'horas_trabajo_semana',
        ]

        widgets = {
            'alumno': forms.Select(attrs={
                'class': 'form-select',
            }),

            'materia': forms.Select(attrs={
                'class': 'form-select',
            }),

            'horas_clase_semana': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1 - 10',
                'min': '1',
                'max': '10',
            }),

            'promedio_general_anterior': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10, ej. 8.5',
                'min': '0',
                'max': '10',
                'step': '0.1',
            }),

            'materias_reprobadas_previas': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10',
                'min': '0',
                'max': '10',
            }),

            'promedio_materia_anterior': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10, ej. 7.8',
                'min': '0',
                'max': '10',
                'step': '0.1',
            }),

            'parcial_1': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10, ej. 8.0',
                'min': '0',
                'max': '10',
                'step': '0.1',
            }),

            'parcial_2': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10, ej. 8.5',
                'min': '0',
                'max': '10',
                'step': '0.1',
            }),

            'promedio_tareas': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10, ej. 9.0',
                'min': '0',
                'max': '10',
                'step': '0.1',
            }),

            'porcentaje_tareas_entregadas': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 100, ej. 85',
                'min': '0',
                'max': '100',
                'step': '0.1',
            }),

            'participacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10, ej. 7.5',
                'min': '0',
                'max': '10',
                'step': '0.1',
            }),

            'conducta': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 10, ej. 9',
                'min': '0',
                'max': '10',
                'step': '0.1',
            }),

            'faltas_materia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 30',
                'min': '0',
                'max': '30',
            }),

            'retardos_materia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 30',
                'min': '0',
                'max': '30',
            }),

            'asistencia_porcentaje': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 100, ej. 95',
                'min': '0',
                'max': '100',
                'step': '0.1',
            }),

            'horas_estudio_semana_materia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 20, ej. 4',
                'min': '0',
                'max': '20',
                'step': '0.1',
            }),

            'apoyo_familiar_nivel': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1 = bajo, 2 = medio, 3 = alto',
                'min': '1',
                'max': '3',
            }),

            'acceso_internet': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),

            'trabaja': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),

            'horas_trabajo_semana': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0 - 48',
                'min': '0',
                'max': '48',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['alumno'].empty_label = 'Selecciona un alumno'
        self.fields['materia'].empty_label = 'Selecciona primero un alumno'

        self.fields['materia'].queryset = Materia.objects.none()

        if 'alumno' in self.data:
            try:
                alumno_id = int(self.data.get('alumno'))
                alumno = Alumno.objects.get(id=alumno_id)

                self.fields['materia'].queryset = Materia.objects.filter(
                    grado=alumno.grado
                ).order_by('nombre_materia')

            except (ValueError, TypeError, Alumno.DoesNotExist):
                self.fields['materia'].queryset = Materia.objects.none()

    def clean(self):
        cleaned_data = super().clean()

        alumno = cleaned_data.get('alumno')
        materia = cleaned_data.get('materia')

        if alumno and materia:
            if alumno.grado != materia.grado:
                raise forms.ValidationError(
                    'La materia seleccionada no corresponde al grado del alumno.'
                )

        return cleaned_data