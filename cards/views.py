from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect

from cards.cards import Cards
from cards.forms.player import PlayerForm
from cards.drinks import Drinks
from cards.db_utils import DBUtils


def play_game(request):
    cards = Cards()
    drinks = Drinks()
    players = request.session.get('players', [])
    template = loader.get_template('cards/playgame.html')

    player_cards = cards.get_cards_for_players(players)
    loser = cards.get_loser(player_cards)[0]
    player_drinks = {}
    for player in players:
        player_drinks[player] = drinks.get_player_drink(player)

    DBUtils().save_round(loser)

    return HttpResponse(template.render(
        {"player_cards": player_cards, "loser": loser, "player_drinks": player_drinks},
        request, ))


def get_players(players):
    if players:
        return players.split(",")
    return ["unknown"]


def register_players(request):
    template = loader.get_template('cards/registerplayers.html')

    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            DBUtils().save_drink_and_player(form)

            return HttpResponse(template.render(
                {"form": form, "name": form.cleaned_data['name']},
                request,))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlayerForm()

    return HttpResponse(template.render(
        {"form": form},
        request,))


def save_player_to_session(request, player):
    """ Save a player name to the session

    The session is used within the request object,
    saving the player here means it can be accessed by other
    views.

    :param request: request
    :param player: String
    :return:
    """
    sessionlist = request.session.get('players', [])
    sessionlist.append(player)
    request.session['players'] = sessionlist


def player_list(request):
    set_session_expiry(request)
    template = loader.get_template('cards/playerlist.html')
    render_data = {
        "in_game": [],
        "players": [],
    }

    if request.method == "POST":
        if request.POST.get("go"):
            return redirect("play")
        # Adds player to session (To register for game)
        save_player_to_session(request, request.POST["player_name"])
        render_data["in_game"] = request.session['players']
    else:
        render_data["in_game"] = request.session.get('players', [])

    players = DBUtils().get_all_players()

    # Could probably refactor all below.
    # Adds all players to the list
    for player in players:
        render_data["players"].append(player.name)

    # Removes players already playing
    for playing in render_data["in_game"]:
        if playing in render_data["players"]:
            render_data["players"].remove(playing)

    return HttpResponse(
        template.render(
            render_data, request,))


def set_session_expiry(request):
    request.session.set_expiry(5)


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