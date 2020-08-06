from rest_framework import viewsets
from .models import HotelRoom
from .serializers import HotelRoomSerializer


class HotelRoomViewSet(viewsets.ModelViewSet):
    """Manage Recipe in the database"""
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer

