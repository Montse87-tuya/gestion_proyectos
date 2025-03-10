from django import forms
from .models import Proyecto, Tarea, Mensaje, Comentario, Grupo, Rol, Notificacion

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = '__all__'