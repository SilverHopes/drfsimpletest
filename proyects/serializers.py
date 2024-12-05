from rest_framework import serializers
from .models import Proyect

class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'titulo', 'rut', 'nombre_apellido', 'created_at')
        read_only_fields = ('created_at',)
        