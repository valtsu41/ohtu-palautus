from player import Player, PlayerReader, PlayerStats

from rich import print as rprint
from rich.prompt import Prompt
from rich.table import Table

def main():
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]
    season = Prompt.ask("Season",choices=seasons)
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = Prompt.ask("Nationality", choices=stats.get_nationalities())
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"{nationality} players season {season}")
    table.add_column("Name")
    table.add_column("Team")
    table.add_column("Goals")
    table.add_column("Assists")
    table.add_column("Points")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

    rprint(table)

if __name__ == "__main__":
    main()
