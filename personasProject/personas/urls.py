from django.urls import path
from . import views

urlpatterns = [
    path('', views.persona_lista, name='persona_lista'),
    path('agregar/', views.persona_formulario, name='persona_agregar'),
    path('eliminar/<int:pk>/', views.persona_confirmar_eliminar, name='persona_eliminar'),
    path('detalle/<int:k>/', views.persona_detalle, name='persona_detalle'),
]