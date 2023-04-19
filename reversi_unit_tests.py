import unittest
from model.game import Reversi
from model.reversi_with_ai import ReversiAIProxy
from model.player import Player

class TestReversi(unittest.TestCase):

    def test_initial_board_state(self):
        game = Reversi()
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(game.board.getGrid(), expected)

    def test_valid_move(self):
        game = Reversi()
        self.assertTrue(game.isValidMove([2, 4]))

    def test_invalid_move(self):
        game = Reversi()
        self.assertFalse(game.isValidMove([0, 0]))

    def test_make_move(self):
        game = Reversi()
        game.makeMove([5, 3])
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 2, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(game.board.getGrid(), expected)

    def test_change_cur_player(self):
        game = Reversi()
        game.changeCurPlayer()
        self.assertEqual(game.curPlayer, Player.white)

    def test_possible_moves(self):
        game = Reversi()
        expected = [[2, 4], [3, 5], [4, 2], [5, 3]]
        self.assertEqual(game.possibleMoves(), expected)

    def test_ai_proxy(self):
        game = Reversi()
        ai_game = ReversiAIProxy(game, ai_depth=2)
        ai_move = ai_game.get_ai_move()
        self.assertIn(ai_move, game.possibleMoves())

if __name__ == '__main__':
    unittest.main()