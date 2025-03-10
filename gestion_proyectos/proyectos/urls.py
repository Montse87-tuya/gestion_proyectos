from django.urls import path
from . import views

urlpatterns = [
    # URLs para Proyectos
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/crear/', views.ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto_detail'),
    path('proyectos/<int:pk>/editar/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/<int:pk>/eliminar/', views.ProyectoDeleteView.as_view(), name='proyecto_delete'),

    # URLs para Tareas
    path('tareas/', views.TareaListView.as_view(), name='tarea_list'),
    path('tareas/crear/', views.TareaCreateView.as_view(), name='tarea_create'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detail'),
    path('tareas/<int:pk>/editar/', views.TareaUpdateView.as_view(), name='tarea_update'),
    path('tareas/<int:pk>/eliminar/', views.TareaDeleteView.as_view(), name='tarea_delete'),

    # URLs para Mensajes
    path('mensajes/', views.MensajeListView.as_view(), name='mensaje_list'),
    path('mensajes/crear/', views.MensajeCreateView.as_view(), name='mensaje_create'),

    # URLs para Comentarios
    path('comentarios/', views.ComentarioListView.as_view(), name='comentario_list'),
    path('comentarios/crear/', views.ComentarioCreateView.as_view(), name='comentario_create'),

    # URLs para Grupos
    path('grupos/', views.GrupoListView.as_view(), name='grupo_list'),
    path('grupos/crear/', views.GrupoCreateView.as_view(), name='grupo_create'),

    # URLs para Roles
    path('roles/', views.RolListView.as_view(), name='rol_list'),
    path('roles/crear/', views.RolCreateView.as_view(), name='rol_create'),

    # URLs para Notificaciones
    path('notificaciones/', views.NotificacionListView.as_view(), name='notificacion_list'),
    path('notificaciones/<int:pk>/editar/', views.NotificacionUpdateView.as_view(), name='notificacion_update'),
]