from django import forms
from .models import Carpeta, Proyecto, Tarea

class CarpetaForm(forms.ModelForm):
    class Meta:
        model = Carpeta
        fields = ['titulo']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'fecha_limite']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'fecha_limite']
