from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelRoomViewSet


router = DefaultRouter()
router.register('rooms', HotelRoomViewSet)

app_name = 'hotel'

urlpatterns = [
    path('', include(router.urls)),
]
