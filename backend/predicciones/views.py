from django.shortcuts import get_object_or_404, redirect, render

from .forms import PrediccionMateriaForm
from .models import PrediccionMateria
from .services.predictor import predecir_tercer_parcial


def lista_predicciones(request):
    predicciones = (
        PrediccionMateria.objects
        .select_related(
            "alumno",
            "materia"
        )
        .order_by("-fecha_prediccion")
    )

    contexto = {
        "predicciones": predicciones
    }

    return render(
        request,
        "predicciones/lista_predicciones.html",
        contexto
    )


def crear_prediccion(request):
    if request.method == "POST":
        form = PrediccionMateriaForm(request.POST)

        if form.is_valid():
            try:
                # Crea el objeto, pero todavía no lo guarda.
                prediccion = form.save(commit=False)

                # Reúne las 18 variables esperadas por el modelo.
                datos_modelo = prediccion.obtener_datos_modelo()

                # Ejecuta el modelo de Machine Learning.
                resultado = predecir_tercer_parcial(
                    datos_modelo
                )

                # Resultado central generado por LinearRegression.
                prediccion.calificacion_media_tercer_parcial = (
                    resultado["calificacion_media"]
                )

                # Margen P90 guardado dentro del artefacto.
                prediccion.margen_error_modelo = (
                    resultado["margen_error"]
                )

                # El método save() del modelo calculará:
                # - tercer parcial mínimo y máximo
                # - calificación final mínima, media y máxima
                # - riesgo académico
                prediccion.save()

                return redirect(
                    "detalle_prediccion",
                    prediccion_id=prediccion.id
                )

            except FileNotFoundError as error:
                form.add_error(
                    None,
                    f"No se encontró el modelo de Machine Learning: {error}"
                )

            except ValueError as error:
                form.add_error(
                    None,
                    f"No se pudo generar la predicción: {error}"
                )

            except Exception as error:
                form.add_error(
                    None,
                    "Ocurrió un error inesperado al ejecutar "
                    "el modelo de Machine Learning."
                )

                # Temporalmente útil durante el desarrollo.
                print(
                    "Error al generar la predicción:",
                    error
                )

    else:
        form = PrediccionMateriaForm()

    contexto = {
        "form": form
    }

    return render(
        request,
        "predicciones/crear_prediccion.html",
        contexto
    )


def detalle_prediccion(request, prediccion_id):
    prediccion = get_object_or_404(
        PrediccionMateria.objects.select_related(
            "alumno",
            "materia"
        ),
        id=prediccion_id
    )

    contexto = {
        "prediccion": prediccion
    }

    return render(
        request,
        "predicciones/detalle_prediccion.html",
        contexto
    )