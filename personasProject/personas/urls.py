from django.urls import path
from . import views

urlpatterns = [
    path('', views.persona_formulario, name='persona_formulario'),
        path('personaDatos/<int:k>/', views.persona_detalle, name='persona_detalle'),
]