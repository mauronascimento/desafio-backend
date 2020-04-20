from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import ViagemSerializer, ViagemNotaUpdateSerializer


class ViagemListAPIView(ListAPIView):
    serializer_class = ViagemSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return self.request.user.viagens.all().order_by('data_inicio')


class ViagemNotaUpdateAPIView(UpdateAPIView):
    serializer_class = ViagemNotaUpdateSerializer

    def get_queryset(self):
        return self.request.user.viagens.all()
