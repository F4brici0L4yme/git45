from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'edad', 'donador']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese apellidos'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'min': 17}),
            'donador': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
