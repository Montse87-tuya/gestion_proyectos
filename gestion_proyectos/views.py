from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, Tarea, Mensaje, Comentario
from django.contrib.auth.decorators import login_required
from .forms import ProyectoForm, TareaForm, MensajeForm, ComentarioForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

#Vistas de Proyectos
@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.filter(usuarios=request.user)
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuarios=request.user)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'proyectos/detalle_proyecto.html', {'proyecto': proyecto, 'tareas': tareas})

#Vistas de Tareas
@login_required
def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuarios=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = TareaForm()
    return render(request, 'tareas/crear_tarea.html', {'form': form})

@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tareas/editar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    proyecto_id = tarea.proyecto.id
    tarea.delete()
    return redirect('detalle_proyecto', proyecto_id=proyecto_id)

#Vistas de Mensajes
@login_required
def enviar_mensaje(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuarios=request.user)
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.proyecto = proyecto
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = MensajeForm()
    return render(request, 'mensajes/enviar_mensaje.html', {'form': form})

@login_required
def ver_mensajes(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuarios=request.user)
    mensajes = Mensaje.objects.filter(proyecto=proyecto)
    return render(request, 'mensajes/ver_mensajes.html', {'mensajes': mensajes})

#Vistas de Comentarios
@login_required
def crear_comentario(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.tarea = tarea
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_proyecto', proyecto_id=tarea.proyecto.id)
    else:
        form = ComentarioForm()
    return render(request, 'comentarios/crear_comentario.html', {'form': form})

@login_required
def ver_comentarios(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    comentarios = Comentario.objects.filter(tarea=tarea)
    return render(request, 'comentarios/ver_comentarios.html', {'comentarios': comentarios})

#Vistas de Usuarios y Grupos
@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def lista_grupos(request):
    grupos = Group.objects.all()
    return render(request, 'grupos/lista_grupos.html', {'grupos': grupos})

#Vistas de Autenticación
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_proyectos')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_proyectos')
        else:
            return render(request, 'registration/inicio_sesion.html', {'error': 'Credenciales inválidas'})
    return render(request, 'registration/inicio_sesion.html')

@login_required
def cierre_sesion(request):
    logout(request)
    return redirect('inicio_sesion')