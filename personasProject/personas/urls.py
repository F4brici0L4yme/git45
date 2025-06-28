from django.urls import path
from . import views
from .views import PersonaListView, PersonaUpdateView

urlpatterns = [
    path('', PersonaListView.as_view(), name='persona_lista'),
    path('agregar/', views.persona_formulario, name='persona_agregar'),
    path('eliminar/<int:pk>/', views.persona_confirmar_eliminar, name='persona_eliminar'),
    path('detalle/<int:k>/', views.persona_detalle, name='persona_detalle'),
        path('editar/<int:pk>/', PersonaUpdateView.as_view(), name='persona_editar'),
]