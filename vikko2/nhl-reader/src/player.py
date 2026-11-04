from dataclasses import dataclass

@dataclass
class Player:
    def __init__(self, dict: dict):
        self.name: str = dict['name']
        self.nationality: str = dict['nationality']
        self.assists: int = dict['assists']
        self.goals: int = dict['goals']
        self.team: str = dict['team']
        self.games: int = dict['games']
        self.id: int = dict['id']

    @property
    def score(self) -> int:
        return self.goals + self.assists
    
    def __str__(self) -> str:
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {self.score:2}"
