from rest_api.videogame import GenericCallsSet


class LeagueOfLegends(GenericCallsSet):

    def __init__(self):
        super().__init__('/lol/')

    def get_all_champions(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('champions', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_champion(self, champion_id):
        return self.get_things('champions', some_id=champion_id)

    # ITEMS
    def get_all_items(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('items', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_item(self, item_id):
        return self.get_things('items', some_id=item_id)

    # MASTERIES
    def get_all_masteries(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('masteries', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_mastery(self, mastery_id):
        return self.get_things('masteries', some_id=mastery_id)

    # PLAYERS
    def get_all_players(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('players', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_player(self, player_id):
        return self.get_things('players', some_id=player_id)

    def get_series_players(self, serie_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('series', some_id=serie_id, follow_up_query='players',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_tournament_players(self, tournament_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('tournaments', some_id=tournament_id, follow_up_query='players',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_player_stats(self, player_id):
        return self.get_things('players', some_id=player_id, follow_up_query='stats')

    def get_player_stats_in_serie(self, player_id, serie_id):
        return self.get_things('series', some_id=serie_id, follow_up_query='players/' + str(player_id) + '/stats')

    def get_player_stats_in_tournment(self, player_id, t_id):
        return self.get_things('tournaments', some_id=t_id, follow_up_query='players/' + str(player_id) + '/stats')

    # RUNES
    def get_all_runes(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('runes', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_rune(self, rune_id):
        return self.get_things('runes', some_id=rune_id)

    # SPELLS
    def get_all_spells(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('spells', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_spell(self, spell_id):
        return self.get_things('spells', some_id=spell_id)

    # GAMES
    def get_all_games(self, q_sort=None, q_filter=None, q_range=None):
        """Requires advanced plan on lol"""
        return self.get_things('games', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_game(self, game_id):
        """Requires advanced plan on lol"""
        return self.get_things('games', some_id=game_id)
