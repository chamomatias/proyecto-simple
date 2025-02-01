from django.urls import path
from .views import cursos_create, cursos_read, cursos_read_one, cursos_update, cursos_delete

urlpatterns = [
    path("", cursos_read, name="cursos_lista"),
    path("crear/", cursos_create, name="cursos_crear"),
    path("<int:curso_id>/", cursos_read_one, name="cursos_detalle"),  # Nueva ruta
    path("actualizar/<int:curso_id>/", cursos_update, name="cursos_actualizar"),
    path("eliminar/<int:curso_id>/", cursos_delete, name="cursos_eliminar"),
]
