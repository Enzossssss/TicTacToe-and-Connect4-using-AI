#Imported Libraries
from board import *
from constants import *
from minmax import *

class Match:

    def __init__(self):
        self.human_player = random.randint(1, 2)
        self.player = 1
        self.gameover = False
        self.board = Board()
        if self.human_player == 1: self.ai = MinMax()
        if self.human_player == 2: self.ai = MinMax(1)
    
    def change_player(self):
        """ 
        change the ID of the player.
        """
        self.player = self.player % 2 + 1

    def game_over(self):
        """ 
        set gameover to True if a player win or if the board is full.
        """
        if self.board.check_grid(False) != None:
            self.board.check_grid(True)
            self.gameover = True