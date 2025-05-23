from .models import Contacto
from rest_framework import serializers

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id','nombre','apellido','email','telefono','fotografia']
