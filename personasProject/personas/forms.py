from django import forms

class PersonaForm(forms.Form):
    nombres = forms.CharField(label='Nombres', max_length=100)
    apellidos = forms.CharField(label='Apellidos', max_length=100)
    edad = forms.IntegerField(label='Edad')
    donador = forms.BooleanField(label='¿Es donador?', required=False)