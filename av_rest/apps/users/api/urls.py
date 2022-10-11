from unicodedata import name
from django.urls import path
# sin decorador
# from apps.users.api.api import APIView, UserAPIView
from apps.users.api.api import user_api_view, user_detail_api_view

urlpatterns = [
    # sin decorador
    # path('usuario/', UserAPIView.as_view(), name = 'usuario_api')
    path('usuario/', user_api_view, name = 'usuario_api'),
    path('usuario/<int:pk>/',user_detail_api_view, name = 'usuario_detail_api_view'),
]
