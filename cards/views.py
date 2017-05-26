from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from cards.cards import Cards
 

def index(request):
    cards = Cards()
    template = loader.get_template('cards/index.html')
    raw_players = request.GET.get('players')

    players = get_players(raw_players)
    player_cards = cards.get_cards_for_players(players)
    raw_winner = cards.get_winner(player_cards)
    winner = raw_winner[0]

    return HttpResponse(template.render({"player_cards": player_cards, "winner": winner}, request, ))


def get_players(players):
    return players.split(",")


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