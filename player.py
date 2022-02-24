import math
import random

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
            square = input(self.letter + '/')