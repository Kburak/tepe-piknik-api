from rest_framework import serializers
from .models import HotelRoom


class HotelRoomSerializer(serializers.ModelSerializer):
    """Serializer for the ingredient objects"""

    class Meta:
        model = HotelRoom
        fields = ('__all__')
        read_only_fields = ('id', )
