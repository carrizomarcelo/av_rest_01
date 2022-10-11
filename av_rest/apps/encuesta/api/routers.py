from rest_framework.routers import DefaultRouter
from apps.encuesta.api.views.general_views import *
from apps.encuesta.api.views.encuesta_viewsets import EncuestaViewSet

router = DefaultRouter()

router.register(r'encuestas', EncuestaViewSet, basename='encuestas')
router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'distritos', DistritoViewSet, basename='distritos')
router.register(r'asistencia', IndicadorAsistenciaViewSet, basename='asistencia')

urlpatterns = router.urls