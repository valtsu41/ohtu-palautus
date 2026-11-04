import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()


    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Finnish players:")

    res_players = sorted(
        filter(lambda p: p.nationality == "FIN", players),
        key=lambda p: p.score,
        reverse=True
    )

    for player in res_players:
        print(player)

if __name__ == "__main__":
    main()
