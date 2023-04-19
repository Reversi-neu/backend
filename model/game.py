from model.player import Player
from model.board import Board
from model.classic_mode import ClassicMode
from model.reversi_interface import ReversiInterface
from model.game_prototype import GamePrototype

# Reversi class - the main class of the game
class Reversi(ReversiInterface, GamePrototype):
    # ai_depth 0 means no AI in game
    def __init__(self, size=8, gameLogic=None): 
        if gameLogic is None:
                gameLogic = ClassicMode()

        self.board = Board(size, board=[])
        self.boardSize = size
        self.curPlayer = Player.black
        self.gameLogic = gameLogic
        self.player1Score = 2
        self.player2Score = 2

        self.gameLogic.getSize(size)

        self.board.__setitem__([int(size / 2) - 1, int((size / 2) - 1)], Player.black.value)
        self.board.__setitem__([int((size / 2) - 1), int(size / 2)], Player.white.value)
        self.board.__setitem__([int(size / 2), int((size / 2) - 1)], Player.white.value)
        self.board.__setitem__([int(size / 2), int(size / 2)], Player.black.value)

    # Check if the move is valid, return False if not valid
    def isValidMove(self, move):
        # returns False if not valid
        return self.gameLogic.isMovePossible(self.board.getGrid(), move, self.curPlayer.value)
    
    # Make a move on the board
    def makeMove(self, move):
        gainedTiles = self.gameLogic.makeMove(self.board.getGrid(), move, self.curPlayer.value)

        for tile in gainedTiles:
            self.board.__setitem__(tile, self.curPlayer.value)
    
    # Change the current player
    def changeCurPlayer(self):
        if self.curPlayer == Player.black:
            self.curPlayer = Player.white
        else:
            self.curPlayer = Player.black
    
    # Checks for a winner, returns 0 if no winner, 1 if player 1 won, 2 if player 2 won
    def checkWin(self):
        self.player1Score = 0
        self.player2Score = 0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board.__getitem__([i, j]) == 1:
                    self.player1Score += 1
                elif self.board.__getitem__([i, j]) == 2:
                    self.player2Score += 1

        # string of game state
        return  self.gameLogic.checkWin(self.board.getGrid())

    # Gets the array of possible moves
    def possibleMoves(self):
        # array of moves [0, 0]
        return self.gameLogic.possibleMoves(self.board.getGrid(), self.curPlayer.value)

    # DESIGN PATTERN: Prototype
    def copy(self):
        copiedGame = Reversi(self.boardSize, self.gameLogic)
        copiedGame.board = Board(self.boardSize, board=[row.copy() for row in self.board.getGrid()])
        copiedGame.curPlayer = self.curPlayer
        copiedGame.player1Score = self.player1Score
        copiedGame.player2Score = self.player2Score
        return copiedGame
