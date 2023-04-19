import unittest
from model.games_manager import GamesManager
from model.player import Player
from model.game import Reversi
from model.reversi_with_ai import ReversiAIProxy
from flask import json

class TestGamesManager(unittest.TestCase):

    def setUp(self):
        self.gamesManager = GamesManager(1)

    def test_createGame(self):
        player1 = {'userID': 1, 'username': 'player1'}
        player2 = {'userID': 2, 'username': 'player2'}
        size = 8
        gameType = 'local'
        difficulty = 0

        game_created = self.gamesManager.createGame(player1, player2, size, gameType, difficulty)
        game_dict = json.loads(game_created.data)  # Convert the JSON response to a Python dictionary

        self.assertEqual(game_dict['id'], 1)
        self.assertEqual(game_dict['type'], 'local')
        self.assertEqual(game_dict['size'], 8)
        self.assertEqual(game_dict['player1'], player1)
        self.assertEqual(game_dict['player2'], player2)

    def test_makeMove(self):
        player1 = {'userID': 1, 'username': 'player1'}
        player2 = {'userID': 2, 'username': 'player2'}
        size = 8
        gameType = 'local'
        difficulty = 0

        game_created = self.gamesManager.createGame(player1, player2, size, gameType, difficulty)
        game_dict = json.loads(game_created.data)

        move = {"x": 2, "y": 3}
        game_after_move = self.gamesManager.makeMove(gameType, game_dict['id'], move)
        game_after_move_dict = json.loads(game_after_move.data)  # Convert the JSON response to a Python dictionary

        self.assertEqual(game_after_move_dict['board'][2][3], 1)

    def test_getGamesByTypeByUserID(self):
        self.gamesManager.createGame(self.player1, self.player2, 8, "online", 0)
        self.gamesManager.createGame(self.player1, self.player2, 8, "ai", 1)

        player1_online_games = self.gamesManager.getGamesByTypeByUserID("online", 1)
        self.assertEqual(len(player1_online_games), 1)
        self.assertEqual(player1_online_games[0]["type"], "online")

        player1_ai_games = self.gamesManager.getGamesByTypeByUserID("ai", 1)
        self.assertEqual(len(player1_ai_games), 1)
        self.assertEqual(player1_ai_games[0]["type"], "ai")

    def test_getGameByID(self):
        game = self.gamesManager.createGame(self.player1, self.player2, 8, "online", 0)
        game_id = game["id"]

        fetched_game = self.gamesManager.getGameByID(game_id)
        self.assertEqual(fetched_game["id"], game_id)
        self.assertEqual(fetched_game["player1"], self.player1)
        self.assertEqual(fetched_game["player2"], self.player2)

if __name__ == '__main__':
    unittest.main()
