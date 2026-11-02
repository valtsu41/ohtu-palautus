import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.player_reader = PlayerReaderStub()
        self.stats = StatisticsService(
            self.player_reader
        )

    def test_search(self):
        res = self.stats.search("Semenko")

        self.assertIsNotNone(res)
        self.assertEqual(res.name, "Semenko")
        self.assertEqual(res.team, "EDM")
        self.assertEqual(res.goals, 4)
        self.assertEqual(res.assists, 12)

    def test_fake_search(self):
        res = self.stats.search("SKIBIDI TOILET")
        self.assertIsNone(res)

    def test_team(self):
        res = self.stats.team("EDM")
        names = map(lambda x: x.name, res)
        self.assertSequenceEqual(list(names), ["Semenko", "Kurri", "Gretzky"])

    def test_fake_team(self):
        res = self.stats.team("SIX-SEVEN FIGHTERS")
        self.assertSequenceEqual(res, [])

    def test_top_points(self):
        res = self.stats.top(4)
        names = map(lambda x: x.name, res)
        self.assertSequenceEqual(list(names), ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"])

    def test_top_goals(self):
        res = self.stats.top(4, SortBy.GOALS)
        names = map(lambda x: x.name, res)
        self.assertSequenceEqual(list(names), ["Lemieux", "Yzerman", "Kurri", "Gretzky", "Semenko"])

    def test_top_assists(self):
        res = self.stats.top(4, SortBy.ASSISTS)
        names = map(lambda x: x.name, res)
        self.assertSequenceEqual(list(names), [ "Gretzky", "Yzerman", "Lemieux", "Kurri", "Semenko"])