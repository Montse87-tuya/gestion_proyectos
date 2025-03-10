from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Proyecto, Tarea, Mensaje, Comentario, Grupo, Rol, Notificacion
from .forms import ProyectoForm, TareaForm, MensajeForm, ComentarioForm, GrupoForm, RolForm, NotificacionForm

class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'proyectos/proyecto_list.html'
    context_object_name = 'proyectos'

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyectos/proyecto_detail.html'
    context_object_name = 'proyecto'

class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'proyectos/proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')

# Vistas para Tareas (similar a Proyectos)
class TareaListView(ListView):
    model = Tarea
    template_name = 'proyectos/tarea_list.html'
    context_object_name = 'tareas'

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'proyectos/tarea_detail.html'
    context_object_name = 'tarea'

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'proyectos/tarea_form.html'
    success_url = reverse_lazy('tarea_list')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class TareaUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'proyectos/tarea_form.html'
    success_url = reverse_lazy('tarea_list')

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'proyectos/tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea_list')

class MensajeCreateView(CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'proyectos/mensaje_form.html'
    success_url = reverse_lazy('mensaje_list')

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        return super().form_valid(form)

class MensajeListView(ListView):
    model = Mensaje
    template_name = 'proyectos/mensaje_list.html'
    context_object_name = 'mensajes'

# Vistas para Comentarios (similar a Mensajes)
class ComentarioCreateView(CreateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'proyectos/comentario_form.html'
    success_url = reverse_lazy('comentario_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ComentarioListView(ListView):
    model = Comentario
    template_name = 'proyectos/comentario_list.html'
    context_object_name = 'comentarios'

class GrupoCreateView(CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'proyectos/grupo_form.html'
    success_url = reverse_lazy('grupo_list')

class GrupoListView(ListView):
    model = Grupo
    template_name = 'proyectos/grupo_list.html'
    context_object_name = 'grupos'

# Vistas para Roles (similar a Grupos)
class RolCreateView(CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'proyectos/rol_form.html'
    success_url = reverse_lazy('rol_list')

class RolListView(ListView):
    model = Rol
    template_name = 'proyectos/rol_list.html'
    context_object_name = 'roles'

class NotificacionListView(ListView):
    model = Notificacion
    template_name = 'proyectos/notificacion_list.html'
    context_object_name = 'notificaciones'

class NotificacionUpdateView(UpdateView):
    model = Notificacion
    form_class = NotificacionForm
    template_name = 'proyectos/notificacion_form.html'
    success_url = reverse_lazy('notificacion_list')         


