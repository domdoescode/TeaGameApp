from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=200, unique=True)
    drink_preference = models.OneToOneField(
        DrinkRequirements,
    )


class DrinkRequirements(models.Model):
    mug_clean = models.BooleanField(default=False)

    drink_choices = (
        ("Tea", 'tea'),
        ("Coffee", 'coffee'),
    )

    drink_type = models.CharField(
        max_length=20,
        choices=drink_choices,
        default='NA',
    )

    milk = models.BooleanField(deafult=True)
    sugar = models.IntegerField(default=0)


class Round(models.Model):

    date = models.DateTimeField(auto_now_add=True)

    players = models.ForeignKey(
        Player,
        related_name="round_players",
    )

    loser = models.OneToOneField(
        Player,
        related_name="round_loser",
    )
