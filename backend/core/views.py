# core/views.py
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
