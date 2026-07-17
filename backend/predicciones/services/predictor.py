from functools import lru_cache
from pathlib import Path

import joblib
import pandas as pd
from django.conf import settings


NOMBRE_ARCHIVO_MODELO = (
    "modelo_edupredict_tercer_parcial_v1.joblib"
)


@lru_cache(maxsize=1)
def cargar_artefacto():
    """
    Carga el modelo una sola vez mientras el servidor
    de Django permanezca encendido.
    """

    ruta_modelo = (
        Path(settings.BASE_DIR)
        / "modelos_ml"
        / NOMBRE_ARCHIVO_MODELO
    )

    if not ruta_modelo.exists():
        raise FileNotFoundError(
            f"No se encontró el modelo en: {ruta_modelo}"
        )

    artefacto = joblib.load(ruta_modelo)

    claves_requeridas = {
        "modelo",
        "columnas",
        "metricas",
        "informacion",
    }

    claves_faltantes = (
        claves_requeridas - set(artefacto.keys())
    )

    if claves_faltantes:
        raise ValueError(
            "El artefacto no contiene las claves: "
            + ", ".join(sorted(claves_faltantes))
        )

    return artefacto


def predecir_tercer_parcial(datos: dict) -> dict:
    """
    Recibe las 18 variables académicas y devuelve
    la predicción central, su rango y las métricas
    principales del modelo.
    """

    artefacto = cargar_artefacto()

    modelo = artefacto["modelo"]
    columnas = artefacto["columnas"]
    metricas = artefacto["metricas"]

    columnas_faltantes = [
        columna
        for columna in columnas
        if columna not in datos
    ]

    if columnas_faltantes:
        raise ValueError(
            "Faltan variables requeridas: "
            + ", ".join(columnas_faltantes)
        )

    fila = {
        columna: datos[columna]
        for columna in columnas
    }

    dataframe = pd.DataFrame(
        [fila],
        columns=columnas
    )

    prediccion = float(
        modelo.predict(dataframe)[0]
    )

    # La escala de calificaciones es de 0 a 10.
    prediccion = max(
        0.0,
        min(10.0, prediccion)
    )

    margen = float(
        metricas["margen_error_p90"]
    )

    minima = max(
        0.0,
        prediccion - margen
    )

    maxima = min(
        10.0,
        prediccion + margen
    )

    return {
        "calificacion_minima": round(minima, 2),
        "calificacion_media": round(prediccion, 2),
        "calificacion_maxima": round(maxima, 2),
        "margen_error": margen,
        "mae": float(metricas["mae"]),
        "rmse": float(metricas["rmse"]),
        "r2": float(metricas["r2"]),
    }