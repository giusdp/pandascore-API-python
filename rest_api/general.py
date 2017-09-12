from rest_api.videogame import GenericCallsSet


class GeneralPanda(GenericCallsSet):

    def __init__(self):
        super().__init__()

    # LEAGUES
    def get_all_leagues(self, q_sort=None, q_filter=None, q_range=None):
        """Return all the leagues. They can be sorted, filtered
        :param q_sort: a list of string with one or more of the following strings:
        id, image, default_serie_id, url, name, videogame_id, created_at, updated_at, slug.
        It sorts the response with the attributes selected, use minus (-) for a reversed sort. 
        Sorted by id desc by default.
        :type q_sort: list
        :param q_filter: a dict to specify what to use for filtering with the keys being a string which is the field 
        to filter and the value for each key is a list of string.
        :type q_filter: dict
        :param q_range: to be done"""
        return self.get_things('/leagues', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_videogame_leagues(self, videogame_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/videogames/', some_id=videogame_id, follow_up_query='/leagues',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_league(self, league_id):
        return self.get_things('/leagues/', some_id=league_id)

    # MATCHES
    def get_matches_in_tournament(self, tournament_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/tournaments/', some_id=tournament_id, follow_up_query='/matches',
                                        query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_matches_of_team(self, team_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/teams/', some_id=team_id, follow_up_query='/matches',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_all_matches(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/matches', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_match(self, match_id):
        return self.get_things('/matches', some_id=match_id)

    # PLAYERS
    def get_all_players(self,q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/players', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_players_in_match(self, match_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/matches/', some_id=match_id, follow_up_query='/players',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get__player(self, player_id):
        return self.get_things('/players/', some_id=player_id)

    # SERIES
    def get_all_series(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/series', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_videogame_series(self, videogame_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/videogames/', some_id=str(videogame_id), follow_up_query='/series',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_league_series(self, league_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/league/', some_id=league_id, follow_up_query='/series',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_series(self, series_id):
        return self.get_things('/series/', some_id=series_id)

    # TEAMS
    def get_teams_in_tournament(self, tournament_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/tournaments/', some_id=tournament_id, follow_up_query='/teams',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_teams_in_match(self, match_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/matches/', some_id=match_id, follow_up_query='/teams',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_all_teams(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/teams', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_team(self, team_id):
        return self.get_things('/teams/', some_id=team_id)

    # TOURNAMENTS
    def get_tournaments_in_videogames(self, videogame_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/videogames/', some_id=videogame_id, follow_up_query='/tournaments',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_tournaments_in_league(self, league_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/leagues/', some_id=league_id, follow_up_query='/tournaments',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_tournaments_in_serie(self, serie_id, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/series/', some_id=serie_id, follow_up_query='/tournaments',
                               query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_all_tournaments(self, q_sort=None, q_filter=None, q_range=None):
        return self.get_things('/tournaments', query_sort=q_sort, query_filter=q_filter, query_range=q_range)

    def get_tournament(self, tournament_id):
        return self.get_things('/tournaments/', some_id=tournament_id)

    # VIDEOGAMES
    def get_all_videogames(self, q_sort=None, q_filter=None, q_range=None):
        return self.rest_api.send_query('/videogames', query_sort=q_sort, query_filter=q_filter, query_range=q_range)
