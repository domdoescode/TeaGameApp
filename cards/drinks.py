from datastore.models import Player


class Drinks:

    def get_player_drink(self, player):
        """ Gets the drink details for a player

        Calls the database to get the player object,
        then gets the players drink preference.

        "milk" and "sugar" are then converted to values
        which are appropriate for the front-end.

        :param player: String
        :return: dict
        """

        player = Player.objects.get(name=player)
        return {
            "drink": player.drink_preference.drink_type.capitalize(),
            "milk": self.get_milk_string(player.drink_preference.milk),
            "sugar": self.get_sugar_string(player.drink_preference.sugar)
        }

    @staticmethod
    def get_milk_string(milk):
        """ Returns a normalised string for milk.

        "milk" as a bool does not look good on the front end,
        so this method converts it to a front-end friendly version.

        milk == true - milk == "" so that it will become "with milk" or "with no milk".

        :param milk: bool
        :return: String
        """
        if milk:
            return ""
        return "no"

    @staticmethod
    def get_sugar_string(sugar):
        """ Returns a normalised string for sugar.

        "sugar" as a int does not look good on the front end, if
        the user wants no sugar. So instead the 0 value is converted
        to "no".
        This results in "The user wants no sugar", or "the user wants 1 sugar".

        :param sugar: int
        :return: string
        """
        if sugar == 0:
            return "no"
        return str(sugar)
