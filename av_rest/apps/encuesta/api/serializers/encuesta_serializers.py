from rest_framework import serializers

from apps.encuesta.models import Departamento, Encuesta
from apps.encuesta.api.serializers.general_serializers import DepartamentoSerializer, DistritoSerializer

class EncuestaSerializer(serializers.ModelSerializer):
    # departamento = serializers.StringRelatedField()
    # distrito = serializers.StringRelatedField()
    
    
    class Meta:
        model = Encuesta
        exclude = ('state', 'create_date', 'modified_date', 'delete_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'last_name': instance.last_name,
            'du': instance.du,
            #'image': instance.image if instance.image != '' else '',
            'departamento': instance.departamento.dpto if instance.departamento is not None else '' ,
            'distrito': instance.distrito.distrito if instance.distrito is not None else ''
        }