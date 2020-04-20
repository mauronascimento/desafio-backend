from django.urls import path
from .views import ViagemListAPIView, ViagemNotaUpdateAPIView


urlpatterns = [
    path(
        '',
        ViagemListAPIView.as_view(),
        name='list'
    ),
    path(
        '<int:pk>/',
        ViagemNotaUpdateAPIView.as_view(),
        name='update'
    ),
]