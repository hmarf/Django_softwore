from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    room_type = models.CharField(max_length=30)

class Booking(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel_id = models.ForeignKey(Hotel,on_delete=models.CASCADE, null=True)
    time_data = models.DateTimeField(null=True)