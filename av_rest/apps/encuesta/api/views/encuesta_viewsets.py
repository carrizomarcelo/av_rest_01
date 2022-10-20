from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.users.authentication_mixins import Authentication

from apps.encuesta.api.serializers.encuesta_serializers import EncuestaSerializer

class EncuestaViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = EncuestaSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()

    def list(self, request):
        encuesta_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(encuesta_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Encuesta creada correctamente!'}, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            encuesta_serializer = self.serializer_class(self.get_queryset(pk),data=request.data)
            if encuesta_serializer.is_valid():
                encuesta_serializer.save()
                return Response(encuesta_serializer.data, status=status.HTTP_200_OK)
            return Response(encuesta_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        encuesta = self.get_queryset().filter(id = pk).first()
        if encuesta:
            encuesta.state = False
            encuesta.save()
            return Response({'message': 'Encuesta eliminada correctamnete!'},status = status.HTTP_200_OK)
        return Response({'error': 'No existe una encuesta con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    

# class EncuestaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = EncuestaSerializer
 
#     def patch(self,request,pk=None):
#         if self.get_queryset(pk):
#             encuesta_serializer = self.serializer_class(self.get_queryset(pk))
#             return Response(encuesta_serializer.data,status = status.HTTP_200_OK)
#         return Response({'error': 'No existe una encuesta con estos datos!'},status=status.HTTP_400_BAD_REQUEST)
    
    

    