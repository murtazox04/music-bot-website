from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import AudioSerializer
from .models import Audio
from .pagination import CustomPagination


class AudioModelViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    pagination_class = None
    http_method_names = ['get', 'post']


# class AudioListView(generics.ListAPIView):
#     queryset = Audio.objects.all()
#     serializer_class = AudioSerializer
#     # pagination_class = CustomPagination
#     filter_backends = filters.SearchFilter
#     search_fields = ['title', ]

class AudioListDetailfilter(generics.ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']


class AudioSearch(generics.ListAPIView):
    permission_classes = [CustomPagination]
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
