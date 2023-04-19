# Reversi AI class - AI implementation for Reversi game
class ReversiAI:
    def __init__(self, depth):
        self.depth = depth

    # Returns the best move for the AI
    def get_best_move(self, game):
        possibleMoves = game.possibleMoves()
        if not possibleMoves:
            return None

        bestMove = None
        bestScore = float('-inf')

        for move in possibleMoves:
            newGame = game.copy()
            newGame.makeMove(move)
            newGame.changeCurPlayer()
            newGame.checkWin()

            score = self.minimax(newGame, self.depth, False)

            print(f"Move: {move}, Score: {score}")

            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestMove

        #print(possibleMoves)
        #print(game.board.get_grid())
        #print(game.player1_score)
        #print(game.player2_score)

        #return possibleMoves[0]

    # Minimax algorithm for AI - returns the best score for the AI
    def minimax(self, game, depth, maximizing):
        if depth == 0 or game.checkWin():
            if game.curPlayer == 1:
                return game.player1Score - game.player2Score
            else:
                return game.player2Score - game.player1Score

        if maximizing:
            maxEval = float('-inf')
            
            for move in game.possibleMoves():
                newGame = game.copy()
                newGame.makeMove(move)
                newGame.changeCurPlayer()
                newGame.checkWin()
                
                eval = self.minimax(newGame, depth-1, False)
                maxEval = max(maxEval, eval)

            return maxEval

        else:
            minEval = float('inf')

            for move in game.possibleMoves():
                newGame = game.copy()
                newGame.makeMove(move)
                newGame.changeCurPlayer()
                newGame.checkWin()
                
                eval = self.minimax(newGame, depth-1, True)
                minEval = min(minEval, eval)

            return minEval
