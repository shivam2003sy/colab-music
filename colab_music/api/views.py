

# Create your views here.
from rest_framework import generics
from .models import Room

from .serializers import RoomSerializers

class Roomview(generics.ListAPIView):
    queryset= Room.objects.all()
    serializer_class=RoomSerializers