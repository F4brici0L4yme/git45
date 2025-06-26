from django.urls import path
from . import views

urlpatterns = [
    path('', views.persona_formulario, name='persona_formulario'),
]