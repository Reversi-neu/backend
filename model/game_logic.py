from abc import ABC, abstractmethod

# Interface for game logic
class GameLogic(ABC):
    def __init__(self):
        self.size = 8

    @abstractmethod
    def getSize(self, s):
        pass

    @abstractmethod
    def isMovePossible(self, board, move, player):
        pass

    @abstractmethod
    def makeMove(self, board, move, player):
        pass

    @abstractmethod
    def possibleMoves(self, board, player):
        pass

    @abstractmethod
    def checkWin(self, board):
        pass

    
