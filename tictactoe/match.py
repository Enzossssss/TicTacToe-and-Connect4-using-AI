#Imported Libraries
import pygame
import random
from board import *
from constants import *
from minmax import MinMax

class Match:

    def __init__(self):
        self.human_player = random.randint(1, 2)
        self.player = 1
        self.board = Board()
        if self.human_player == 1: self.ai = MinMax()
        if self.human_player == 2: self.ai = MinMax(1, True)
        self.gameover = True

    def change_player(self):
        """ 
        change the ID of the player.
        """
        self.player = self.player % 2 + 1

    def game_over(self):
        """ 
        return True if a player win or if the board is full.
        """
        return self.board.check_grid(True) != 0 or self.board.signed == 9

    def print_figure(self, row, column):
        """ 
        print the current turn figure (O or X) into the choosen square.

        Parameters
        ----------
        row : int value, row coordinate of the choosen square
        column : int value, column coordinate of the choosen square
        """
        if self.player == 1:
            pygame.draw.line(board, WHITE, (column * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20), (column * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), 10)
            pygame.draw.line(board, WHITE, (column * SQUARE_SIZE + 20, row * SQUARE_SIZE + SQUARE_SIZE - 20), (column * SQUARE_SIZE + SQUARE_SIZE - 20, row * SQUARE_SIZE + 20), 10)
        else:
            pygame.draw.circle(board, WHITE, (column * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 70, 8)