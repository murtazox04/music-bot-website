from django.urls import path, include
from .views import AudioModelViewSet, AudioListDetailfilter

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'audios', AudioModelViewSet, basename='audio')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', AudioListDetailfilter.as_view(), name='audiosearch'),
]
