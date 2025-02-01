from django.db import models

class Cursos(models.Model):
    """
    Modelo que representa un curso.
    """
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    duracion_semanas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.duracion_semanas} semanas)"

    class Meta:
        ordering = ["nombre"]  # Ordena los cursos alfabéticamente
