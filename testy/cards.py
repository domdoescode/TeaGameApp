__author__ = "MissMaximas"

import random


class Cards:

    cards = ["Two", "Three", 
            "Four", "Five", "Six", 
            "Seven", "Eight", "Nine", "Ten",
             "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Spades", "Diamonds", "Hearts"]

    def get_card(self):
        cards_idx = random.randint(0, 12)
        suits_idx = random.randint(0, 3)
        return self.cards[cards_idx], self.suits[suits_idx]


# Testing
c = Cards()
card, suit = c.get_card()
print(card + " of " +  suit)