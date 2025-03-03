import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

def load_game_data(filename='chess_data.csv'):
    data = pd.read_csv(filename)
    return data

def process_game_data(data):
    moves = data['moves'].apply(lambda x: x.split())
    labels = moves.apply(lambda x: x[-1] if len(x) > 1 else None)
    move_encoder = LabelEncoder()
    all_moves = [move for sublist in moves for move in sublist]
    move_encoder.fit(all_moves)
    encoded_labels = move_encoder.transform(labels)
    return moves, encoded_labels, move_encoder