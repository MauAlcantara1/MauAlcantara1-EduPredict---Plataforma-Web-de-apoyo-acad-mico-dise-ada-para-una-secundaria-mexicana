from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from alumnos.models import Alumno
from materias.models import Materia


class PrediccionMateria(models.Model):
    RIESGO_CHOICES = [
        ('BAJO', 'Bajo'),
        ('MEDIO', 'Medio'),
        ('ALTO', 'Alto'),
    ]

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='predicciones'
    )

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='predicciones'
    )

    # Variables del Modelo 3
    horas_clase_semana = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    promedio_general_anterior = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    materias_reprobadas_previas = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    promedio_materia_anterior = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    parcial_1 = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    parcial_2 = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    promedio_tareas = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    porcentaje_tareas_entregadas = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    participacion = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    conducta = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    faltas_materia = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(30)]
    )

    retardos_materia = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(30)]
    )

    asistencia_porcentaje = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    horas_estudio_semana_materia = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )

    apoyo_familiar_nivel = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )

    acceso_internet = models.BooleanField()

    trabaja = models.BooleanField()

    horas_trabajo_semana = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(48)]
    )

    # Resultado generado por el modelo
    calificacion_tercer_parcial_estimada = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    riesgo_academico = models.CharField(
        max_length=10,
        choices=RIESGO_CHOICES,
        blank=True,
        null=True
    )

    observacion = models.TextField(blank=True, null=True)

    fecha_prediccion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Predicción por materia'
        verbose_name_plural = 'Predicciones por materia'
        ordering = ['-fecha_prediccion']


    def calcular_riesgo(self):
        if self.calificacion_tercer_parcial_estimada < 6:
            return 'ALTO'
        elif self.calificacion_tercer_parcial_estimada < 7.5:
            return 'MEDIO'
        else:
            return 'BAJO'

    def calcular_estimacion_provisional(self):
        estimacion = (
            self.parcial_1 * 0.30 +
            self.parcial_2 * 0.40 +
            self.promedio_tareas * 0.10 +
            self.participacion * 0.05 +
            self.conducta * 0.05 +
            (self.asistencia_porcentaje / 10) * 0.10
        )

        return round(max(0, min(10, estimacion)), 2)

    def save(self, *args, **kwargs):
        self.calificacion_tercer_parcial_estimada = self.calcular_estimacion_provisional()
        self.riesgo_academico = self.calcular_riesgo()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.alumno} - {self.materia} - {self.calificacion_tercer_parcial_estimada}"