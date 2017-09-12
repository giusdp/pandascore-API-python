import unittest

from rest_api import apimediator
from rest_api import general
from rest_api import lol

ITEMS_IN_LEAGUE = 6


class TestPandaRest(unittest.TestCase):

    def setUp(self):
        self.rest_api = apimediator.PandaRestAPI()
        self.panda = general.GeneralPanda()
        self.lol = lol.LeagueOfLegends()

    def test_build_query(self):
        self.assertEqual(self.rest_api.encode_options('test', {'sort': ['test']}), 'test?sort=test')
        self.assertEqual(self.rest_api.encode_options('test', {}), 'test')
        a = self.rest_api.encode_options('test', {'sort': []})
        self.assertEqual(a, 'test')

    def test_send_query(self):
        self.assertRaises(TypeError, self.rest_api.send_query, None)
        self.assertRaises(TypeError, self.rest_api.send_query, 12)
        self.assertRaises(TypeError, self.rest_api.send_query, 'test', 12)

    def test_query_leagues_no_params(self):
        result = self.panda.get_all_leagues()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 200)
        self.assertEqual(apimediator.get_status_message(result[0]), 'Ok',
                         'Status Message in resulting tuple is not Ok.')

    def test_query_leagues_with_id(self):
        result = self.panda.get_league(4000)
        self.assertEqual(result[0], 200)
        self.assertEqual(ITEMS_IN_LEAGUE, len(result[1]), 'Json response has more than 1 league')

    def test_query_leagues_sort_filter(self):
        result = self.panda.get_all_leagues(['id', '-name'])
        self.assertEqual(result[0], 200)
        result = self.panda.get_all_leagues(['id', '-name'], {'id': [4000]})
        self.assertEqual(result[0], 200)

    def test_games_leagues(self):
        result = self.panda.get_videogame_leagues(3)
        self.assertEqual(result[0], 200)

    def test_matches_tournament_team(self):
        result = self.panda.get_matches_in_tournament(410, [])
        self.assertEqual(result[0], 200)
        result = self.panda.get_matches_of_team(18, [])
        self.assertEqual(result[0], 200)
        result = self.panda.get_all_matches()
        self.assertEqual(result[0], 200)

    def test_lol(self):
        result = self.lol.get_all_champions([], {})
        self.assertEqual(result[0], 200)
        result = self.lol.get_mastery(74)
        self.assertEqual(result[0], 200)
        result = self.lol.get_tournament_players(410)
        self.assertEqual(result[0], 200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
