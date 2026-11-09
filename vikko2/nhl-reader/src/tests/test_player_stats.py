"""Unit tests for PlayerStats that use only local player data."""

import unittest

from src.player import Player, PlayerStats


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            Player("Alex", "CAN", 20, 30, "AAA", 82),
            Player("Blake", "USA", 35, 10, "BBB", 82),
            Player("Casey", "CAN", 15, 25, "AAA", 80),
            Player("Drew", None, None, None, None, 10),
        ]
        self.stats = PlayerStats(self.players)

    def test_get_nationalities_returns_unique_known_values(self):
        self.assertEqual(
            set(self.stats.get_nationalities()),
            {"CAN", "USA"}
        )

    def test_get_teams_returns_unique_known_values(self):
        self.assertEqual(set(self.stats.get_teams()), {"AAA", "BBB"})

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual([player.name for player in result], ["Alex", "Casey"])

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        result = self.stats.top_scorers_by_team("AAA")

        self.assertEqual([player.name for player in result], ["Alex", "Casey"])

    def test_top_scorers_by_team_returns_empty_for_unknown_team(self):
        self.assertEqual(self.stats.top_scorers_by_team("UNKNOWN"), [])

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in result], ["Alex", "Casey"])

    def test_top_goal_scorers_treats_missing_goals_as_zero(self):
        result = self.stats.top_goal_scorers(4)

        self.assertEqual([player.name for player in result][-1], "Drew")


if __name__ == "__main__":
    unittest.main()
