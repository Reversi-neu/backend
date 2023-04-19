class ConsoleGameView():

    def __init__(self):
        self.width = 0

    def get_game_size(self):
        self.width = int(input("Input game size: "))

        return self.width
        
    def print_board(self, board, current_player):
        print("Turn: Player", current_player)
        for i in range(self.width):
            print(board[i])
                
    def get_user_input(self):
        col = int(input("Input col: "))
        row = int(input("Input row: "))

        return row, col

    def print_winner(self, player1, player2):
        winner = ''
        if player1 > player2:
            winner = "Player 1 Wins!"
        elif player2 > player1:
            winner = "Player 2 Wins!"
        else:
            winner = "TIE"
        print(winner)

    def print_score(self, player1, player2):
        print("Score:", player1, "--", player2)

    def print_moves(self, possibleMoves):
        print("Possible Moves:", possibleMoves)

    def print_invalid_move(self):
        print("Invalid move")
