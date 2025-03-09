from django.db import models
from django.contrib.auth.models import User, Group

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuarios = models.ManyToManyField(User, related_name='proyectos')
    administrador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos_administrados')

    def __str__(self):
        return self.titulo
    
class Tarea(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    usuarios_asignados = models.ManyToManyField(User, related_name='tareas_asignadas')

    def __str__(self):
        return self.titulo

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos', null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='mensajes', null=True, blank=True)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'De {self.remitente} a {self.destinatario or self.proyecto}'

class Comentario(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario en {self.tarea} por {self.usuario}'
    
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    permisos = models.TextField() # Aquí puedes almacenar permisos en formato JSON o similar

    def __str__(self):
        return self.nombre
    
class GrupoProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='grupos_proyecto')
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.grupo.name} en {self.proyecto.titulo}'