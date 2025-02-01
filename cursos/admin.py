from django.contrib import admin
from .models import Cursos

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duracion_semanas")
    search_fields = ("nombre",)
