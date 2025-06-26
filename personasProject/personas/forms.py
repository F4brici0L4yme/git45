from django import forms
from .models import Persona
from django.shortcuts import render

class PersonaForm(forms.Form):
    nombres = forms.CharField(
        label='Nombres',
        max_length=100,
        initial='Este es'
    )
    apellidos = forms.CharField(label='Apellidos', max_length=100, initial='un ejemplo de initialValue')
    edad = forms.IntegerField(label='Edad')
    donador = forms.BooleanField(label='¿Es donador?', required=False)

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 18:
            raise forms.ValidationError("Debes tener al menos 18 años.")
        return edad