

from rest_framework import serializers
from .models import Menu,Booking



class BookingSeralizer(serializers.ModelSerializer):
  class Meta:
    model = Booking
    fields = "__all__"
    

class MenuSeralizer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = "__all__"