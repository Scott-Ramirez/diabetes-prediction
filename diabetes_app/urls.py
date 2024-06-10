from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prediction_interface.urls')),  # Incluye las URLs de la aplicación prediction_interface
]
