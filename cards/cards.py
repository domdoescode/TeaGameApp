__author__ = "MissMaximas"

import random
from collections import OrderedDict


class Cards:

    cards = ["Two", "Three",
            "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten",
             "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]

    def get_card(self):
        cards_idx = random.randint(0, 12)
        suits_idx = random.randint(0, 3)
        return self.cards[cards_idx], self.suits[suits_idx], \
               cards_idx+2, suits_idx

    def get_cards_for_players(self, players):
        """ Retrieve cards for each player

        :param players: list [string]
        :return: dict {string:dict}
        """

        players_cards = {}

        for player in players:
            card, suit, card_idx, suit_idx = self.get_card()
            players_cards[player] = {
                "card": card,
                "suit": suit,
                "card_idx":  card_idx,
                "suit_idx": suit_idx,
            }
        return players_cards

    @staticmethod
    def sorted_players(player_cards):
        return sorted(player_cards.items(), key=lambda item: item[1]['card_idx'])

    def get_winner(self, player_cards):
        sp = self.sorted_players(player_cards)
        return sp[len(sp)-1]
