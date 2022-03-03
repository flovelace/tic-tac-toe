import math

class Player:
    def __init__(self, letter): # letter is x or o
        self.letter = letter
    
    # we want all of the players to get to their next move
    def get_move(self, game):
        pass

class randomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # this is going to check that this is value by trying to cast
            # it to an integer, and it's not, then we say that it's invalid
            # if that spot is not available on the board, we will also say that it's invalid
            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        
        return val