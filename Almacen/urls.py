"""
URL configuration for Almacen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoALmacen import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    
    # Niños
    path('lista-niños/', views.lista_niños, name='lista_niños'),
    path('crear-niño/', views.crear_niño, name='crear_niño'),
    path('editar-niño/<int:id>/', views.editar_niño, name='editar_niño'),
    path('borrar-niño/<int:id>/', views.borrar_niño, name='borrar_niño'),
    
    # Padres
    path('lista-padres/', views.lista_padres, name='lista_padres'),
    path('crear-padre/', views.crear_padre, name='crear_padre'),
    path('editar-padre/<int:id>/', views.editar_padre, name='editar_padre'),
    path('borrar-padre/<int:id>/', views.borrar_padre, name='borrar_padre'),
    
    # Clases
    path('lista-clases/', views.lista_clases, name='lista_clases'),
    path('crear-clase/', views.crear_clase, name='crear_clase'),
    path('editar-clase/<int:id>/', views.editar_clase, name='editar_clase'),
    path('borrar-clase/<int:id>/', views.borrar_clase, name='borrar_clase'),
]
