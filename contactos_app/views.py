from django.shortcuts import render
from rest_framework import viewsets
from .models import Contacto
from .serializers import ContactoSerializer
from rest_framework.exceptions import ValidationError

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
        