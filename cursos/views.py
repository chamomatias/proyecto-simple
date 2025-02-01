from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cursos
from .forms import CursoCreateForm, CursoUpdateForm, CursoReadForm

@login_required
def cursos_create(request):
    """Crea un nuevo curso."""
    if request.method == "POST":
        form = CursoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cursos_lista")
    else:
        form = CursoCreateForm()

    return render(request, "cursos/cursos-crear.html", {"form": form})

@login_required
def cursos_read(request):
    """Lista todos los cursos."""
    cursos = Cursos.objects.all()
    return render(request, "cursos/cursos-lista.html", {"cursos": cursos})

@login_required
def cursos_read_one(request, curso_id):
    """Muestra un solo curso sin permitir edición."""
    curso = get_object_or_404(Cursos, id=curso_id)
    form = CursoReadForm(instance=curso)
    return render(request, "cursos/cursos-detalle.html", {"form": form, "curso": curso})

@login_required
def cursos_update(request, curso_id):
    """Edita un curso existente."""
    curso = get_object_or_404(Cursos, id=curso_id)

    if request.method == "POST":
        form = CursoUpdateForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("cursos_lista")
    else:
        form = CursoUpdateForm(instance=curso)

    return render(request, "cursos/cursos-actualizar.html", {"form": form, "curso": curso})

@login_required
def cursos_delete(request, curso_id):
    """Confirma la eliminación de un curso antes de borrarlo definitivamente."""
    curso = get_object_or_404(Cursos, id=curso_id)

    if request.method == "POST":  # Si el usuario confirma, se elimina
        curso.delete()
        return redirect("cursos_lista")

    return render(request, "cursos/cursos-eliminar.html", {"curso": curso})
