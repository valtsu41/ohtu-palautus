from dataclasses import dataclass
import requests

@dataclass
class Player:
    name: str | None
    nationality: str | None
    assists: int | None
    goals: int | None
    team: str | None
    games: int | None

    @property
    def points(self) -> int | None:
        if self.goals is None or self.assists is None:
            return None
        return self.goals + self.assists

def get_players(url) -> list[Player]:
    response = requests.get(url, timeout=10).json()
    res = []
    for obj in response:
        res.append(Player(
            obj.get("name"),
            obj.get("nationality"),
            obj.get("assists"),
            obj.get("goals"),
            obj.get("team"),
            obj.get("games")
        ))
    return res


class PlayerStats():
    def __init__(self, players: list[Player]):
        self.players = players

    def get_nationalities(self) -> list[str]:
        res = {p.nationality for p in self.players if p.nationality is not None}
        return list(res)

    def get_teams(self) -> list[str]:
        res = {p.team for p in self.players if p.team is not None}
        return list(res)

    def top_scorers_by_nationality(self, nationality: str) -> list[Player]:
        return sorted(
            filter(lambda p: p.nationality == nationality, self.players),
            key=lambda p: p.points or 0,
            reverse=True
        )

    def top_scorers_by_team(self, team: str) -> list[Player]:
        return sorted(
            (p for p in self.players if p.team == team),
            key=lambda p: p.points or 0,
            reverse=True
        )

    def top_goal_scorers(self, how_many):
        """Palauttaa enintään how_many eniten maaleja tehnyttä pelaajaa.

        Pelaajat järjestetään maalimäärän mukaan laskevaan järjestykseen.
        """
        return sorted(
            self.players,
            key=lambda p: p.goals or 0,
            reverse=True
        )[:how_many]
