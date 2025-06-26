from django.shortcuts import render
from .forms import PersonaForm

def persona_formulario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            return render(request, 'confirmacion.html', {'datos': datos})
    else:
        form = PersonaForm()
    
    return render(request, 'formulario.html', {'form': form})