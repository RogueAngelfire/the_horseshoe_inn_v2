from django.db import models

    
    
ROOM_TYPES = (
        ('Single-Room', 'Single-Room'),
        ('Double-Room', 'Double-Room'),
        ('Family-Room', 'Family-Room'),
    )  

class RoomInformation(models.Model):
    
    class Meta:
        verbose_name_plural = 'RoomInformation'

    room_name = models.CharField(max_length=15, choices=ROOM_TYPES, default='None')
    room_image = models.ImageField(upload_to="media/rooms_images")
    room_description = models.CharField(max_length=255)
    room_type = models.CharField(max_length=100)
    room_ratings = models.IntegerField(default=1)
    room_price_per_night = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.room_name
    
    def delete(self, *args, **kwargs):
        self.room_image.delete()
        super().delete(*args, **kwargs)
