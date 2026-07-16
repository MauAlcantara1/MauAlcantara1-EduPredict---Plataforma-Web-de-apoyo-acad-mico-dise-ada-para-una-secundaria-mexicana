from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Materia(models.Model):
    GRADO_CHOICES = [
        (1, 'Primero'),
        (2, 'Segundo'),
        (3, 'Tercero'),
    ]

    nombre_materia = models.CharField(max_length=100)
    area_materia = models.CharField(max_length=100)

    grado = models.PositiveSmallIntegerField(
        choices=GRADO_CHOICES
    )

    dificultad_materia = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    horas_clase_semana = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    class Meta:
        unique_together = ('nombre_materia', 'grado')
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return f"{self.nombre_materia} - {self.get_grado_display()}"