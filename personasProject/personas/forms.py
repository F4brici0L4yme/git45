from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'edad', 'donador']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese apellidos'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'donador': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 18:
            raise forms.ValidationError("Debes tener al menos 18 años.")
        return edad