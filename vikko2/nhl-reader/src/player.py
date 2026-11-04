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
    
    def __str__(self):
        return f"{self.name} team {self.team} points {self.goals}+{self.assists}"
