from datastore.models import Round, Player, DrinkRequirements


class DBUtils:

    @staticmethod
    def save_round(loser):
        """ Saves a Round entry in the DB.

        Saves a round entry, using the loser passed in.

        :param loser: string
        :return:
        """
        round = Round()
        round.loser = loser
        round.save()

    @staticmethod
    def save_drink_and_player(form):
        """ Cleans form data and saves to DB

        :param form: form
        :return:
        """
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

    @staticmethod
    def get_all_players():
        """ Gets all players from the database

        :return: django object
        """
        return Player.objects.all()
