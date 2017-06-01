from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response

from cards.cards import Cards
from datastore.models import Round, Player, DrinkRequirements
from cards.forms.player import PlayerForm


def play_game(request):
    cards = Cards()
    template = loader.get_template('cards/playgame.html')
    players = get_players(request.GET.get('players'))

    player_cards = cards.get_cards_for_players(players)
    loser = cards.get_loser(player_cards)[0]

    save_round(loser)

    return HttpResponse(template.render(
        {"player_cards": player_cards, "loser": loser},
        request, ))


def save_round(loser):
    round = Round()
    round.loser = loser
    round.save()


def get_players(players):
    if players:
        return players.split(",")
    return ["unknown"]


def register_players(request):
    template = loader.get_template('cards/registerplayers.html')

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            save_drink_and_player(form)

            return HttpResponse(template.render(
                {"form": form, "name": form.cleaned_data['name']},
                request,))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlayerForm()

    return HttpResponse(template.render(
        {"form": form},
        request,))


def save_drink_and_player(form):
    name = form.cleaned_data['name']
    drink_type = form.cleaned_data['drink_type']
    milk = form.cleaned_data["milk"]
    sugar = form.cleaned_data['sugar']

    drink = DrinkRequirements()
    drink.drink_type = drink_type
    drink.milk = milk
    drink.sugar = sugar
    drink.save()

    player = Player()
    player.name = name
    player.drink_preference = drink
    player.save()


def player_list(request):
    # player = Player()
    template = loader.get_template('cards/playerlist.html')

    available_players = []
    players = Player.objects.all()
    for player in players:
        available_players.append(player.name)

    return HttpResponse(
        template.render(
            {"players": available_players
             }, request, ))


class GetCards(APIView):

  def get(self, request, format=None):
    """
    Return a hardcoded response.
    """
    c = Cards()
    card, suit, card_idx, suit_idx = c.get_card()
    return Response({
        "card": card,
        "suit": suit,
        "card_idx": card_idx
    })