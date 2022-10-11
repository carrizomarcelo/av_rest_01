from rest_framework import viewsets
from rest_framework.response import Response

from apps.encuesta.models import Departamento, Distrito, IndicadorAsistencia
from apps.encuesta.api.serializers.general_serializers import DepartamentoSerializer, DistritoSerializer, IndicadorAsistenciaSerializer

class DepartamentoViewSet(viewsets.GenericViewSet):
    model = Departamento
    serializer_class = DepartamentoSerializer

    def get_queryset(self):
        return self.get_serializer().Metal.model.objects.filter(state = True)

    def list(self, request):
        """
        Listado de Departamentos


        Sin información

        """


        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)

class DistritoViewSet(viewsets.GenericViewSet):
    model = Distrito
    serializer_class = DistritoSerializer

    def get_queryset(self):
        return self.get_serializer().Metal.model.objects.filter(state = True)

    def list(self, request):
        """
        Listado de Distritos


        Sin información

        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)


class IndicadorAsistenciaViewSet(viewsets.GenericViewSet):
    model = IndicadorAsistencia
    serializer_class = IndicadorAsistenciaSerializer

    def get_queryset(self):
        return self.get_serializer().Metal.model.objects.filter(state = True)

    def list(self, request):
        """
        Listado de Asistencias


        Sin información

        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)
        return Response(data.data)
