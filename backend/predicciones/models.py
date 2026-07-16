from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from alumnos.models import Alumno
from materias.models import Materia


class PrediccionMateria(models.Model):
    MARGEN_ERROR_MODELO = 0.7

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

    # Resultados del tercer parcial
    calificacion_minima_tercer_parcial = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    calificacion_media_tercer_parcial = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    calificacion_maxima_tercer_parcial = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    # Resultados de la calificación final
    calificacion_final_minima = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    calificacion_final_media = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    calificacion_final_maxima = models.FloatField(
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
        """
        Determina el riesgo utilizando el rango completo
        de la calificación final.
        """

        if (
            self.calificacion_final_minima is None
            or self.calificacion_final_maxima is None
        ):
            return None

        # Incluso en el mejor escenario reprueba.
        if self.calificacion_final_maxima < 6:
            return 'ALTO'

        # Incluso en el peor escenario obtiene al menos 7.5.
        if self.calificacion_final_minima >= 7.5:
            return 'BAJO'

        # Existe incertidumbre o una calificación baja.
        return 'MEDIO'


    def calcular_estimacion_provisional(self):
        """
        Fórmula temporal utilizada mientras se conecta
        el modelo real de Machine Learning.
        """

        estimacion = (
            self.parcial_1 * 0.30
            + self.parcial_2 * 0.40
            + self.promedio_tareas * 0.10
            + self.participacion * 0.05
            + self.conducta * 0.05
            + (self.asistencia_porcentaje / 10) * 0.10
        )

        return round(max(0, min(10, estimacion)), 2)


    def calcular_rango_tercer_parcial(self):
        """
        Calcula los escenarios mínimo, medio y máximo
        del tercer parcial.
        """

        if self.calificacion_media_tercer_parcial is None:
            return None, None, None

        media = self.calificacion_media_tercer_parcial
        margen = self.MARGEN_ERROR_MODELO

        minima = max(0, media - margen)
        maxima = min(10, media + margen)

        return (
            round(minima, 2),
            round(media, 2),
            round(maxima, 2)
        )


    def calcular_rango_calificacion_final(self):
        """
        Calcula la calificación final mínima, media y máxima
        usando los tres escenarios del tercer parcial.
        """

        if (
            self.calificacion_minima_tercer_parcial is None
            or self.calificacion_media_tercer_parcial is None
            or self.calificacion_maxima_tercer_parcial is None
        ):
            return None, None, None

        final_minima = (
            self.parcial_1
            + self.parcial_2
            + self.calificacion_minima_tercer_parcial
        ) / 3

        final_media = (
            self.parcial_1
            + self.parcial_2
            + self.calificacion_media_tercer_parcial
        ) / 3

        final_maxima = (
            self.parcial_1
            + self.parcial_2
            + self.calificacion_maxima_tercer_parcial
        ) / 3

        return (
            round(max(0, min(10, final_minima)), 2),
            round(max(0, min(10, final_media)), 2),
            round(max(0, min(10, final_maxima)), 2)
        )


    def save(self, *args, **kwargs):
        # Temporalmente se usa esta fórmula.
        # Después será sustituida por la predicción del modelo de ML.
        if self.calificacion_media_tercer_parcial is None:
            self.calificacion_media_tercer_parcial = (
                self.calcular_estimacion_provisional()
            )

        (
            self.calificacion_minima_tercer_parcial,
            self.calificacion_media_tercer_parcial,
            self.calificacion_maxima_tercer_parcial
        ) = self.calcular_rango_tercer_parcial()

        (
            self.calificacion_final_minima,
            self.calificacion_final_media,
            self.calificacion_final_maxima
        ) = self.calcular_rango_calificacion_final()

        self.riesgo_academico = self.calcular_riesgo()

        super().save(*args, **kwargs)


    def __str__(self):
        return (
            f"{self.alumno} - {self.materia} - "
            f"{self.calificacion_media_tercer_parcial}"
        )