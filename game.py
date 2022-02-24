class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # use a single list to represent 3x3 board
        self.current_winner = None # keeps track of the winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what index corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    #    moves = []
    #    for (i, x) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
       #     if spot == ' ':
       #         moves.append(i)
       #     return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_square(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    # iterate while the game still has empty square
    # we don't have to determine the winner because it will be returned
    # which breaks the loop
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # define the function to make a move
        if game.make_move(square, letter):
           if print_game:
               print(letter + f' makes a move to square {square}')
               game.print_board()
               print('') # an empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after move is made, alternate letters
            letter = 'O' if letter == 'X' else 'X' # switch player
        
        if print_game:
            print('It\'s a tie')

