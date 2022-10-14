#Imported Libraries
import pygame
from constants import *
import numpy as np

# initialize the board
pygame.init()
board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

#Draw grid lines
pygame.draw.line(board, WHITE, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_SIZE)
pygame.draw.line(board, WHITE, (WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE, HEIGHT), LINE_SIZE)
pygame.draw.line(board, WHITE, (0,SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_SIZE)
pygame.draw.line(board, WHITE, (0, HEIGHT - SQUARE_SIZE), (WIDTH, HEIGHT - SQUARE_SIZE), LINE_SIZE)

class Board:

    def __init__(self):
        self.grid = np.zeros((ROWS, COLUMNS))
        self.signed = 0

    def sign(self, row, column, player):
        """ 
        sign the player into the choosen squre of the grid.

        Parameters
        ----------
        row : int value, row coordinate of the choosen square
        column : int value, column coordinate of the choosen square
        player : int value, ID of the player (1 or 2)
        """
        self.grid[row][column] = player
        self.signed += 1

    def its_empty(self, row, column):
        """ 
        return True if the choosen squre is empty, False otherwise.

        Parameters
        ----------
        row : int value, row coordinate of the choosen square
        column : int value, column coordinate of the choosen square
        """
        return self.grid[row][column] == 0

    def free_position(self):
        """ 
        return a list of the remain empty positions.
        """
        return [(i, j) for i in range(3) for j in range(3) if self.grid[i][j] == 0]

    def check_grid(self, win):
        """ 
        check if a player win the game, if win parameter is setted to True it also show the victory with a red line.

        Parameters
        ----------
        win : boolean value, show the victory with a red line.
        """
        for i in range(ROWS):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0:
                if win: self.print_victory('row', i)
                return self.grid[i][0]

        for i in range(COLUMNS):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                if win: self.print_victory('column', i)
                return self.grid[0][i]

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            if win: self.print_victory('diagonal-1')
            return self.grid[1][1]
        
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0:
            if win: self.print_victory('diagonal-2')
            return self.grid[1][1]

        return 0 
    
    def print_victory(self, type, start = 0):
        """ 
        show the victory with a red line.

        Parameters
        ----------
        type : string value, type of the victory (column, row, diagonal-1 or diagonal-2).
        """
        if type == 'column':
            pygame.draw.line(board, RED, (start * SQUARE_SIZE + SQUARE_SIZE // 2, 20), (start * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 20), 5)
        if type == 'row':
            pygame.draw.line(board, RED, (20, start * SQUARE_SIZE + SQUARE_SIZE // 2), (WIDTH - 20, start * SQUARE_SIZE + SQUARE_SIZE // 2), 5)
        if type == 'diagonal-1':
            pygame.draw.line(board, RED, (20, 20), (WIDTH - 20, HEIGHT - 20), 5)
        if type == 'diagonal-2':
            pygame.draw.line(board, RED, (20, HEIGHT - 20), (WIDTH - 20, 20), 5)