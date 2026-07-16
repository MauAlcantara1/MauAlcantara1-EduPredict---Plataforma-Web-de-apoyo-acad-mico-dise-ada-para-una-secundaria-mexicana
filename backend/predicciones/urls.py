from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_predicciones, name='lista_predicciones'),
    path('nuevo/', views.crear_prediccion, name='crear_prediccion'),
    path('<int:prediccion_id>/', views.detalle_prediccion, name='detalle_prediccion'),
]