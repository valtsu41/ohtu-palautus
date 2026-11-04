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
        else:
            return self.goals + self.assists

    def __str__(self) -> str:
        return f"{self.name:20} {self.team:15} {self.goals:>2} + {self.assists:<2} = {self.points:<2}"

class PlayerReader():
    def __init__(self, url: str):
        self.url = url

    def get_players(self) -> list[Player]:
        response = requests.get(self.url).json()
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
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()

    def get_nationalities(self) -> list[str]:
        res = {p.nationality for p in self.players if p.nationality is not None}
        return list(res)

    def top_scorers_by_nationality(self, nationality: str):
        return sorted(
            filter(lambda p: p.nationality == nationality, self.players),
            key=lambda p: p.points or 0,
            reverse=True
        )