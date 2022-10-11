from dataclasses import field
from apps.encuesta.models import Departamento, Distrito, IndicadorAsistencia

from rest_framework import serializers

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        exclude = ('state', 'create_date', 'modified_date', 'delete_date')

class DistritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distrito
        exclude = ('state', 'create_date', 'modified_date', 'delete_date')        


class IndicadorAsistenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = IndicadorAsistencia
        exclude = ('state', 'create_date', 'modified_date', 'delete_date')

