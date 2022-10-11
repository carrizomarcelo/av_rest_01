from django.urls import path

from apps.encuesta.api.views.general_views import DepartamentoListAPIView, DistritoListAPIView, IndicadorAsistenciaListAPIView

urlpatterns = [
    path('departamento', DepartamentoListAPIView.as_view(), name = 'departamento'),
    path('distrito', DistritoListAPIView.as_view(), name = 'distrito'),
    path('asistencia', IndicadorAsistenciaListAPIView.as_view(), name = 'asistencia'),
]
