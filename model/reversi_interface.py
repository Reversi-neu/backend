from abc import ABC, abstractmethod

# Interface for Reversi game
class ReversiInterface(ABC):

    @abstractmethod
    def isValidMove(self, move):
        pass

    @abstractmethod
    def makeMove(self, move):
        pass

    @abstractmethod
    def changeCurPlayer(self):
        pass

    @abstractmethod
    def checkWin(self):
        pass

    @abstractmethod
    def possibleMoves(self):
        pass

    @abstractmethod
    def copy(self):
        pass

