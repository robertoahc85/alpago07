from django.urls import path
from . import views

urlpatterns = [
    path('', views.escuela_list, name='escuela_list'),
    path('escuela/<int:pk>/', views.escuela_detail, name='escuela_detail'),
    path('escuela/nueva/', views.escuela_create, name='escuela_create'),
    path('escuela/<int:pk>/editar/', views.escuela_edit, name='escuela_edit'),
    path('escuela/<int:pk>/eliminar/', views.escuela_delete, name='escuela_delete'),
]
