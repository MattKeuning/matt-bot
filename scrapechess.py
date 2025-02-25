import chess
import chess.pgn
import requests
import pandas as pandas

# Building function to scrape games from Chess.com
def scrape_games(username):
    # I stopped playing online chess in November of 2023 so this is the month I will scrape from
    url: f'https://api.chess.com/pub/player/{username}/games/2023/11'
    # Sends HTTP GET requestion to the URL saving the response in the response variable
    response = requests.get(url)

    # Time to check if the response is valid
    if response.status_code != 200:
        # If we do not get a 200 OK message then something has gone wrong
        print("Failed to fetch data")
        return None

    games_data = response.json()['games']
    game_data = []
    for game in games_data:
        # Getting the pgn data from the given game
        pgn = game['pgn']
        # Reads the PGN into a chess game object to be saved
        game_obj = chess.pgn.read_game(pgn)
        game_data.append(game_obj)

    return game_data

# Saving the game data to a CSV file for easy storage
def save_game_data_to_csv(games, filename='chess_data.csv'):
    data = list()
    for game in games:
        moves = list()
        for move in game.mainline_moves():
            moves.append(str(move))
        data.append({"moves": " ".join(moves)})
    # Creating a pandas DataFrame from the data list
    df = pd.DataFrame(data)
    # Saving DataFrame to CSV file while disabling index column
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    username = 'MattK234'
    games = scrape_games(username)
    if games:
        save_game_data_to_csv(games)