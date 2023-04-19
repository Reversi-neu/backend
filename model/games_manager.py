

import copy
from flask import jsonify
from model.game import Reversi
from model.reversi_with_ai import ReversiAIProxy

# GamesManager class - the class that manages all the games
class GamesManager:

    def __init__(self, gameIdCounter):
        self.games = []
        self.gameIdCounter = gameIdCounter

    # create a new game, returns a jsonified game dict
    def createGame(self, player1, player2, size, gameType, difficulty):
        reversiBoard = ReversiAIProxy(Reversi(size), ai_depth=difficulty) if gameType == 'ai' else Reversi(size)

        # this is basically where we define what our 'games' dicts are gonna look like (THIS IS ALL THE STUFF I WANT FOR THE FRONT END, IT GOTTA BE UPDATED W/ THE GAME)
        game = {
            "id": self.gameIdCounter, 
            "game": reversiBoard, 
            "board": reversiBoard.board.getGrid(),
            "type": gameType, 
            "size": size, 
            "difficulty": difficulty,
            "player1": player1, 
            "player2": player2,
            "winner": None, 
            "player1Score": 2, 
            "player2Score": 2, 
            "currentPlayer": 1, 
            "possibleMoves": reversiBoard.possibleMoves(),
            "active": True
        }
        self.games.append(game)
        self.gameIdCounter += 1

        g_copy = copy.deepcopy(game)
        g_copy.pop('game')
        return jsonify(g_copy)
    
    # makes a move in a game, returns a jsonified game dict
    def makeMove(self, gameType, gameID, move):
        game = list(filter(lambda game: game['id'] == int(gameID), self.games))[0]
        game['game'].makeMove([move["x"], move["y"]])

        # this logic is not good, maybe... either the bot is goated and i suck, or its cheating and i cant tell
        game['game'].changeCurPlayer()
        possibleMoves = game['game'].possibleMoves()
        if (len(possibleMoves) == 0):
            game['game'].changeCurPlayer()
        elif (gameType == 'ai'):
            while True:
                game['game'].makeMove(game['game'].get_ai_move())
                game['game'].changeCurPlayer()
                possibleMoves = game['game'].possibleMoves()
                if game['game'].checkWin(): break
                if (len(possibleMoves) == 0):
                    game['game'].changeCurPlayer()
                else:
                    break
        
        game['winner'] = game['game'].checkWin()
        game['player1Score'] = game['game'].player1Score
        game['player2Score'] = game['game'].player2Score
        game['board'] = game['game'].board.getGrid()
        game['currentPlayer'] = game['game'].curPlayer
        game['possibleMoves'] = game['game'].possibleMoves()

        game_copy = copy.deepcopy(game)
        game_copy.pop('game')
        return jsonify(game_copy)

    # returns a list of all the games with the given gameType and userID
    def getGamesByTypeByUserID(self, gameType, userID):
        playerGames = copy.deepcopy(list(
            filter(lambda game: (game['player1']['userID'] == int(userID) or game['player2']['userID'] == int(userID)) 
                    and game['type'] == gameType, self.games)
        ))
        # need to pop game off here bc its not json serializable
        for game in playerGames:
            game.pop('game')

        return jsonify(playerGames)

    # return a game with the given gameID
    def getGameByID(self, gameID):
        game = copy.deepcopy(list(filter(lambda game: game['id'] == int(gameID), self.games))[0])
        game.pop('game')
        return jsonify(game)