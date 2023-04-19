from model.reversi_interface import ReversiInterface
from model.reversi_ai import ReversiAI
import copy

# ReversiAIProxy class - used for design pattern proxy and AI implementation
class ReversiAIProxy(ReversiInterface):
    def __init__(self, reversi, ai_depth=0):
        self.reversi = reversi
        if ai_depth != 0:
            self.ai = ReversiAI(ai_depth)

    def get_ai_move(self):
        self.reversi.checkWin()
        return self.ai.get_best_move(self.reversi.copy())

    def isValidMove(self, move):
        return self.reversi.isValidMove(move)

    def makeMove(self, move):
        return self.reversi.makeMove(move)

    def changeCurPlayer(self):
        return self.reversi.changeCurPlayer()

    def checkWin(self):
        return self.reversi.checkWin()

    def possibleMoves(self):
        return self.reversi.possibleMoves()

    def copy(self):
        return self.reversi.copy()

    def __getattr__(self, attr):
        if attr == '__deepcopy__':
            return lambda memo: copy.deepcopy(self.reversi, memo)
        return getattr(self.reversi, attr)

