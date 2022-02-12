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
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass