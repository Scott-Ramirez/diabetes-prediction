from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Página de bienvenida
    path('predict_diabetes/', views.predict_diabetes, name='predict_diabetes'),  # Página de formulario de predicción
    # Otras rutas según sea necesario
]
