from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Player, Round, DrinkRequirements
from .serializers import PlayerSerializer, RoundSerializer, DrinkSerialiser


class PlayerList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class RoundList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class DrinkList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = DrinkRequirements.objects.all()
    serializer_class = DrinkSerialiser