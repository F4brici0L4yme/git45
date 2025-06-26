from django.shortcuts import render
from .forms import PersonaForm
from django.shortcuts import redirect

def persona_formulario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save()  # Aquí se guarda en la base de datos
            return redirect('persona_detalle', k=persona.pk)  # Redirige al detalle
    else:
        form = PersonaForm()
    
    return render(request, 'formulario.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Persona

def persona_detalle(request, k):
    persona = get_object_or_404(Persona, pk=k)

    # Calcular el ID anterior y siguiente
    try:
        anterior = Persona.objects.filter(pk__lt=k).order_by('-pk')[0].pk
    except IndexError:
        anterior = None

    try:
        siguiente = Persona.objects.filter(pk__gt=k).order_by('pk')[0].pk
    except IndexError:
        siguiente = None

    contexto = {
        'persona': persona,
        'anterior': anterior,
        'siguiente': siguiente,
    }
    return render(request, 'detalle.html', contexto)
