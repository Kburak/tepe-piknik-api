from django.db import models


class HotelRoom(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    room_size = models.IntegerField()
    available = models.BooleanField(default=True)
    sqrt = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='room-photo')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
