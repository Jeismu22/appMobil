from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarpetaForm, ProyectoForm, TareaForm
from .models import Carpeta, Proyecto, Tarea


def bienvenida(request):
    return render(request, 'bienvenida.html')


def dashboard(request):
    if request.method == 'POST':
        # Crear carpeta
        if 'crear_carpeta' in request.POST:
            form = CarpetaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

        # Crear proyecto
        elif 'crear_proyecto' in request.POST:
            form = ProyectoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

        # Crear tarea
        elif 'crear_tarea' in request.POST:
            form = TareaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')

    # Obtener todas las carpetas, proyectos y tareas para mostrar
    carpetas = Carpeta.objects.all()
    proyectos = Proyecto.objects.all()
    tareas = Tarea.objects.all()

    # Renderizar la página con los formularios y datos
    return render(request, 'dashboard.html', {
        'carpeta_form': CarpetaForm(),
        'proyecto_form': ProyectoForm(),
        'tarea_form': TareaForm(),
        'carpetas': carpetas,
        'proyectos': proyectos,
        'tareas': tareas
    })


# Vista para eliminar un elemento
def eliminar_item(request, modelo, item_id):
    if modelo == 'carpeta':
        item = get_object_or_404(Carpeta, id=item_id)
    elif modelo == 'proyecto':
        item = get_object_or_404(Proyecto, id=item_id)
    elif modelo == 'tarea':
        item = get_object_or_404(Tarea, id=item_id)
    item.delete()
    return redirect('dashboard')


# Vista para editar un elemento
def editar_item(request, modelo, item_id):
    if modelo == 'carpeta':
        item = get_object_or_404(Carpeta, id=item_id)
        form_class = CarpetaForm
    elif modelo == 'proyecto':
        item = get_object_or_404(Proyecto, id=item_id)
        form_class = ProyectoForm
    elif modelo == 'tarea':
        item = get_object_or_404(Tarea, id=item_id)
        form_class = TareaForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = form_class(instance=item)

    return render(request, 'editar_item.html', {'form': form, 'modelo': modelo})
