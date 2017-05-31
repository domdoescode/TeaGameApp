__author__ = "MissMaximas"

from rest_framework import serializers

from .models import Player, Round, DrinkRequirements


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ('id', 'date', 'loser')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'drink_preference')


class DrinkSerialiser(serializers.ModelSerializer):
    class Meta:
        model = DrinkRequirements
        fields = ('id', 'drink_type', 'milk', 'sugar')