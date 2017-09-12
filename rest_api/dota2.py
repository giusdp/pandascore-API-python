from rest_api.apimediator import PandaRestAPI
from rest_api.videogame import GenericCallsSet


class Dota2(GenericCallsSet):

    def __init__(self):
        super().__init__('/dota2/')

    # GAMES
    def get_all_games(self, q_sort=None, q_filter=None, q_range=None):
        """Requires advanced plan on dota 2"""
        return self.get_things('games', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_game(self, game_id):
        """Requires advanced plan on dota 2"""
        return self.get_things('games', some_id=game_id)

    # HEROES
    def get_all_heroes(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('heroes', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_hero(self, hero_id):
        return self.get_things('heroes', some_id=hero_id)

    # ITEMS
    def get_all_items(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('items', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_item(self, item_id):
        return self.get_things('items', some_id=item_id)
