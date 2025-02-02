from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cursos  # ✅ Importamos el modelo correctamente
from . import forms  # ✅ Importamos los formularios correctamente


def inicio(request):
    """Página de inicio."""
    return render(request, "cursos/inicio.html")  # ✅ Renderiza el template correcto


@login_required
def cursos_create(request):
    """Crea un nuevo curso."""
    if request.method == "POST":
        form = forms.CursoCreateForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect("cursos_lista")
    else:
        form = forms.CursoCreateForm()

    return render(request, "cursos/cursos-crear.html", {"form": form})

@login_required
def cursos_read(request):
    """Lista todos los cursos."""
    cursos = Cursos.objects.all()  # ✅ Recuperamos todos los cursos de la BD
    return render(request, "cursos/cursos-lista.html", {"cursos": cursos})

@login_required
def cursos_read_one(request, curso_id):
    """Muestra los detalles de un curso sin edición."""
    curso = get_object_or_404(Cursos, id=curso_id)
    form = forms.CursoReadForm(instance=curso)
    return render(request, "cursos/cursos-detalle.html", {"form": form, "curso": curso})

@login_required
def cursos_update(request, curso_id):
    """Edita un curso existente."""
    curso = get_object_or_404(Cursos, id=curso_id)

    if request.method == "POST":
        form = forms.CursoUpdateForm(request.POST, instance=curso)  
        if form.is_valid():
            form.save()
            return redirect("cursos_lista")
    else:
        form = forms.CursoUpdateForm(instance=curso)

    return render(request, "cursos/cursos-actualizar.html", {"form": form, "curso": curso})

@login_required
def cursos_delete(request, curso_id):
    """Elimina un curso después de una confirmación."""
    curso = get_object_or_404(Cursos, id=curso_id)

    if request.method == "POST":  # Si el usuario confirma, se elimina
        curso.delete()
        return redirect("cursos_lista")

    return render(request, "cursos/cursos-eliminar.html", {"curso": curso})
