from django.db import models


class Alumno(models.Model):
    GRADO_CHOICES = [
        (1, 'Primero'),
        (2, 'Segundo'),
        (3, 'Tercero'),
    ]

    GRUPO_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]

    TURNO_CHOICES = [
        ('MATUTINO', 'Matutino'),
        ('VESPERTINO', 'Vespertino'),
    ]

    SEXO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]

    alumno_id = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)

    grado = models.PositiveSmallIntegerField(choices=GRADO_CHOICES)
    grupo = models.CharField(choices=GRADO_CHOICES)
    turno = models.CharField(max_length=20, choices=TURNO_CHOICES)
    edad = models.PositiveSmallIntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno_id} - {self.nombre} {self.apellidos}"