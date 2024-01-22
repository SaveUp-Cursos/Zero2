# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClienteView.as_view(), name='cliente-list'),
]
