from model.game_logic import GameLogic

# Classic mode game logic, inherits from GameLogic
class ClassicMode(GameLogic):
    DIRECTIONS = [[0, 1], [1, 1], [1, 0], [1, -1],
                  [0, -1], [-1, -1], [-1, 0], [-1, 1]]

    def __init__(self):
        self.size = 8

    def getSize(self, s):
        self.size = s

    def isMoveOnBoard(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def isMovePossible(self, board, move, player):
        x, y = move

        # Check if move is on the board
        if not self.isMoveOnBoard(x, y):
            return False

        # Check if tile picked is empty
        if not board[y][x] == 0 or "":
            return False

        # Check tiles in all directions from selection
        for xDir, yDir in self.DIRECTIONS:
            xpos, ypos = x, y
            xpos += xDir
            ypos += yDir

            # Check if tile is on board 
            if not self.isMoveOnBoard(xpos, ypos):
                continue 

            # Check if next tile is an enemy
            if board[ypos][xpos] == player:
                continue

            # Continues while still enemies
            while board[ypos][xpos] == 3-player:
                xpos += xDir
                ypos += yDir

                # Check if tile is on board
                if not self.isMoveOnBoard(xpos, ypos):
                    break

                # Check if next tile is an enemy
                if board[ypos][xpos] == player:
                    return True

        return False

    def makeMove(self, board, move, player):
        x, y = move
    
        # Store gained tiles before checking in every dir
        gainedTiles = []
        for xDir, yDir in self.DIRECTIONS:
            xpos, ypos = x, y
            xpos += xDir
            ypos += yDir

            # Jump over enemy tiles
            tempArray = []
            if self.isMoveOnBoard(xpos, ypos):
                while board[ypos][xpos] == 3-player:
                    tempArray.append([xpos, ypos])
                    xpos += xDir
                    ypos += yDir

                    # Check if tile is on board
                    if not self.isMoveOnBoard(xpos, ypos):
                        break

                # Player tile after enemy tiles
                if self.isMoveOnBoard(xpos, ypos):
                    if board[ypos][xpos] == player:
                        for tiles in tempArray:
                            gainedTiles.append(tiles)  # Taken tile found



        gainedTiles.append([x, y])     # Original move
        return gainedTiles

    def possibleMoves(self, board, player):
        moves = []

        for i in range(self.size):
            for j in range(self.size):
                if self.isMovePossible(board, [i, j], player):
                    moves.append([i, j])

        return moves

    def checkWin(self, board):
        # Check if current player has no possible moves
        return not self.possibleMoves(board, 1) and not self.possibleMoves(board, 2)

    
