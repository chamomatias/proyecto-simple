from django import forms
from .models import Cursos  # Asegurate de que solo se importe el modelo

class CursoCreateForm(forms.ModelForm):
    """Formulario para crear cursos."""
    class Meta:
        model = Cursos
        fields = ["nombre", "descripcion", "duracion_semanas"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del curso"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "duracion_semanas": forms.NumberInput(attrs={"class": "form-control"}),
        }

class CursoUpdateForm(forms.ModelForm):
    """Formulario para actualizar cursos."""
    class Meta:
        model = Cursos
        fields = ["descripcion", "duracion_semanas"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "duracion_semanas": forms.NumberInput(attrs={"class": "form-control"}),
        }

class CursoReadForm(forms.ModelForm):
    """Formulario solo de lectura para ver un curso."""
    class Meta:
        model = Cursos
        fields = ["nombre", "descripcion", "duracion_semanas"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "readonly": "readonly", "rows": 3}),
            "duracion_semanas": forms.NumberInput(attrs={"class": "form-control", "readonly": "readonly"}),
        }
