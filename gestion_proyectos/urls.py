"""
URL configuration for gestion_proyectos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_proyectos.urls')),  # Incluye las URLs 
    # Proyectos
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),

    # Tareas
    path('proyectos/<int:proyecto_id>/tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),

    # Mensajes
    path('proyectos/<int:proyecto_id>/mensajes/enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('proyectos/<int:proyecto_id>/mensajes/', views.ver_mensajes, name='ver_mensajes'),

    #Comentarios
    path('tareas/<int:tarea_id>/comentarios/crear/', views.crear_comentario, name='crear_comentario'),
    path('tareas/<int:tarea_id>/comentarios/', views.ver_comentarios, name='ver_comentarios'),

    #Usuarios y Grupos
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('grupos/', views.lista_grupos, name='lista_grupos'),

    #Autenticación
     path('registro/', views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cierre_sesion/', views.cierre_sesion, name='cierre_sesion'),
]
