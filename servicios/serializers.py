from rest_framework import serializers
from .models import InscripcionCurso

class InscripcionCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscripcionCurso
        fields = '__all__'