__author__ = "MissMaximas"

from rest_framework import serializers

from .models import Player, Round


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ('date', 'players', 'loser')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'drink_preference')