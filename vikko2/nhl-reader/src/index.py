from rich import print as rprint
from rich.prompt import Prompt
from rich.table import Table

from player import get_players, PlayerStats

SEASONS = [
        "2018-19",
        "2019-20",
        "2020-21",
        "2021-22",
        "2022-23",
        "2023-24",
        "2024-25",
        "2025-26",
        "2026-27"
    ]


def get_selected_players(stats: PlayerStats, season: str):
    selection = Prompt.ask(
        "Search by nationality or team",
        choices=["nationality", "team"]
    )
    if selection == "nationality":
        value = Prompt.ask("Nationality", choices=stats.get_nationalities())
        players = stats.top_scorers_by_nationality(value)
    else:
        value = Prompt.ask("Team", choices=stats.get_teams())
        players = stats.top_scorers_by_team(value)
    return players, f"{value} players season {season}"


def main():
    season = Prompt.ask("Season",choices=SEASONS)

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(get_players(url))

    players, title = get_selected_players(stats, season)

    table = Table(title=title)

    for title in ("Name", "Team", "Goals", "Assists", "Points"):
        table.add_column(title)

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    rprint(table)

if __name__ == "__main__":
    main()
