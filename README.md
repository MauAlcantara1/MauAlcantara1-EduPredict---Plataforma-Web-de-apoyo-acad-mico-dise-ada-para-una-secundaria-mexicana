# Un gusto

Hola :), me presento, soy **MauAlcantara**.

Este proyecto será algo grande y largo, desarrollado con la finalidad de aprender y practicar sobre desarrollo web, Machine Learning, inteligencia artificial aplicada, manejo de datos, automatización de procesos escolares, lectura de documentos PDF, RAG, modelos de lenguaje y buenas prácticas de desarrollo de software.

La idea principal de este proyecto no es solamente construir una aplicación funcional, sino también entender cómo se estructura un sistema completo desde cero: base de datos, backend, frontend, modelo predictivo, carga de archivos, procesamiento de información y generación de reportes inteligentes.

# EduPredict

**EduPredict** es una plataforma web de apoyo académico diseñada para una secundaria mexicana.

El sistema permite registrar alumnos, materias y datos académicos para estimar la calificación del tercer parcial por materia, detectar posibles niveles de riesgo académico y generar información útil para apoyar la toma de decisiones escolares.

La plataforma está pensada como una herramienta de apoyo para personal administrativo, docentes o responsables académicos que buscan identificar de forma temprana a estudiantes que podrían necesitar seguimiento adicional.

## Objetivo del proyecto

El objetivo principal de EduPredict es apoyar la detección temprana de riesgo académico mediante el uso de datos escolares, modelos de Machine Learning y procesamiento inteligente de documentos.

La plataforma permite:

* Registrar alumnos.
* Consultar alumnos registrados.
* Registrar materias por grado escolar.
* Consultar materias disponibles.
* Capturar información académica por alumno y materia.
* Generar una predicción estimada del tercer parcial.
* Clasificar el riesgo académico del alumno.
* Visualizar el detalle de cada predicción.
* Filtrar materias automáticamente según el grado del alumno.
* Cargar archivos PDF estructurados con información académica.
* Extraer datos desde documentos escolares.
* Autollenar formularios a partir de archivos PDF.
* Consultar documentos institucionales para generar recomendaciones.
* Generar reportes académicos claros y explicables.

## Descripción general

EduPredict trabaja con una estructura donde cada predicción corresponde a un alumno en una materia específica.

La unidad principal del sistema es:

```text
1 predicción = 1 alumno en 1 materia
```

Por ejemplo:

```text
Alumno: Juan Pérez
Materia: Matemáticas II
Resultado estimado: 7.4
Riesgo académico: Medio
```

El sistema toma en cuenta información como:

* Promedios anteriores.
* Calificaciones de parcial 1 y parcial 2.
* Promedio de tareas.
* Porcentaje de tareas entregadas.
* Participación.
* Conducta.
* Faltas.
* Retardos.
* Asistencia.
* Horas de estudio.
* Apoyo familiar.
* Acceso a internet.
* Si el alumno trabaja.
* Horas de trabajo por semana.

Con estos datos, EduPredict estima la calificación del tercer parcial y clasifica el nivel de riesgo académico.

## Funcionalidades principales

### Dashboard

El sistema cuenta con un panel principal donde se muestran indicadores generales del sistema, como alumnos registrados, materias disponibles, predicciones realizadas y alumnos con riesgo académico.

### Gestión de alumnos

Permite registrar alumnos con información básica:

* ID del alumno.
* Nombre.
* Apellidos.
* Grado.
* Grupo.
* Turno.
* Edad.
* Sexo.

También permite consultar la lista de alumnos registrados.

### Gestión de materias

EduPredict maneja materias por grado escolar.

Las materias están organizadas para primero, segundo y tercero de secundaria, permitiendo que cada alumno solo pueda ser relacionado con materias correspondientes a su grado.

### Predicciones académicas

El sistema permite capturar información académica del alumno por materia y generar una estimación de la calificación del tercer parcial.

Cada predicción incluye:

* Alumno.
* Materia.
* Datos académicos.
* Datos de asistencia.
* Datos de contexto escolar.
* Calificación estimada.
* Nivel de riesgo académico.
* Fecha de predicción.

### Filtrado dinámico de materias

Cuando el usuario selecciona un alumno en el formulario de predicción, el sistema muestra automáticamente solo las materias correspondientes al grado de ese alumno.

Esto evita errores como asignar una materia de tercero a un alumno de primero.

### Detalle de predicción

Cada predicción cuenta con una vista de detalle donde se muestra:

* Información del alumno.
* Materia evaluada.
* Calificación estimada.
* Riesgo académico.
* Parciales anteriores.
* Datos utilizados para la predicción.

### Modelo de Machine Learning

EduPredict utiliza un modelo de Machine Learning entrenado con datos académicos sintéticos coherentes para estimar la calificación del tercer parcial.

El modelo toma variables académicas y contextuales para generar una predicción numérica entre 0 y 10.

### Clasificación de riesgo académico

A partir de la calificación estimada, el sistema clasifica el riesgo académico del alumno en:

* Bajo.
* Medio.
* Alto.

Esta clasificación permite identificar rápidamente qué estudiantes podrían necesitar seguimiento académico.

### Carga de documentos PDF

El sistema permite subir archivos PDF estructurados con información académica del alumno.

Estos documentos pueden simular formularios escolares o encuestas enviadas a padres de familia, donde se recopilan datos como:

* Materias.
* Horas de estudio.
* Asistencia.
* Tareas.
* Apoyo familiar.
* Acceso a internet.
* Información general del alumno.

### Extracción automática de información

EduPredict extrae información desde los PDF estructurados y la utiliza para autollenar formularios dentro del sistema.

El administrador puede revisar, corregir y confirmar la información antes de guardarla.

### Recomendaciones académicas

El sistema puede consultar documentos institucionales o escolares que contienen recomendaciones para distintos casos de riesgo académico.

Con base en la predicción, los datos del alumno y los documentos disponibles, EduPredict genera recomendaciones más claras y contextualizadas.

## Tecnologías utilizadas

* Python
* Django
* Django REST Framework
* SQLite
* HTML
* CSS
* Bootstrap
* JavaScript
* Pandas
* Scikit-learn
* Joblib
* PyMuPDF / pdfplumber
* RAG
* Modelos de lenguaje
* Git
* GitHub

## Machine Learning

El modelo predictivo se entrena con un dataset sintético diseñado para representar un contexto escolar de secundaria mexicana.

Las variables utilizadas por el modelo incluyen:

```text
horas_clase_semana
promedio_general_anterior
materias_reprobadas_previas
promedio_materia_anterior
parcial_1
parcial_2
promedio_tareas
porcentaje_tareas_entregadas
participacion
conducta
faltas_materia
retardos_materia
asistencia_porcentaje
horas_estudio_semana_materia
apoyo_familiar_nivel
acceso_internet
trabaja
horas_trabajo_semana
```

La variable objetivo es:

```text
calificacion_tercer_parcial
```

El modelo busca estimar la calificación del tercer parcial con base en el desempeño previo y otros factores académicos.

## Estructura general del proyecto

```text
EduPredict/
├── backend/
│   ├── alumnos/
│   ├── materias/
│   ├── predicciones/
│   ├── usuarios/
│   ├── core/
│   ├── config/
│   ├── templates/
│   ├── static/
│   ├── modelo_ml/
│   └── manage.py
├── modelo_ml/
├── notebooks/
├── docs/
├── rag/
├── agente/
├── README.md
└── .gitignore
```

## Instalación local

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd EduPredict
```

Entrar al backend:

```bash
cd backend
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual en Linux o macOS:

```bash
source venv/bin/activate
```

Activar entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear superusuario:

```bash
python manage.py createsuperuser
```

Ejecutar servidor:

```bash
python manage.py runserver
```

Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Uso general

1. Iniciar sesión en el sistema.
2. Registrar alumnos.
3. Verificar materias disponibles.
4. Crear una nueva predicción académica.
5. Seleccionar alumno.
6. Seleccionar materia correspondiente al grado.
7. Capturar datos académicos.
8. Guardar la predicción.
9. Consultar el detalle del resultado.
10. Revisar el riesgo académico estimado.
11. Consultar recomendaciones generadas por el sistema.

## Buenas prácticas utilizadas

Este proyecto busca trabajar con buenas prácticas de desarrollo, incluyendo:

* Separación por aplicaciones en Django.
* Uso de modelos para representar entidades principales.
* Uso de formularios propios.
* Validación de datos.
* Organización de templates.
* Uso de archivos estáticos.
* Separación de lógica de Machine Learning.
* Uso de Git para control de versiones.
* Uso de commits descriptivos.
* Documentación del proyecto.
* Preparación para integración con IA generativa.

## Convención de commits

El repositorio utiliza una convención de commits basada en mensajes descriptivos.

Ejemplos:

```bash
feat: agregar formulario de predicciones
fix: corregir redirección al detalle de predicción
docs: actualizar documentación del proyecto
style: mejorar diseño del dashboard
refactor: separar lógica de predicción
chore: configurar estructura inicial del repositorio
```

Tipos comunes:

```text
feat: nueva funcionalidad
fix: corrección de errores
docs: documentación
style: cambios visuales o formato
refactor: mejora interna del código
chore: configuración o tareas generales
test: pruebas
build: cambios relacionados con construcción o despliegue
```

## Autor

Proyecto desarrollado por **MauAlcantara** como parte de su portafolio de proyectos en desarrollo web, Machine Learning e inteligencia artificial aplicada a educación.
