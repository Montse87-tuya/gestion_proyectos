from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuarios_asignados = models.ManyToManyField(User, related_name='proyectos_asignados')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos_creados')

    def __str__(self):
        return self.titulo

class Tarea(models.Model):
    ESTADOS_TAREA = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS_TAREA, default='pendiente')
    usuarios_asignados = models.ManyToManyField(User, related_name='tareas_asignadas')
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_creadas')

    def __str__(self):
        return self.titulo

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='mensajes', null=True, blank=True)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.emisor} a {self.receptor}'

class Comentario(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.tarea}'

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='grupos')
    usuarios_miembros = models.ManyToManyField(User, related_name='grupos_miembros')

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    permisos_asociados = models.TextField()  # Puedes usar un modelo más complejo para permisos

    def __str__(self):
        return self.nombre

class Notificacion(models.Model):
    usuario_receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    contenido_mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=(('leido', 'Leído'), ('no_leido', 'No Leído')), default='no_leido')

    def __str__(self):
        return f'Notificación para {self.usuario_receptor}'

# Create your models here.
