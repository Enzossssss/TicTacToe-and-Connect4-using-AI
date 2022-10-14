#Imported Libraries
import numpy as np
from constants import *
import pygame

# initialize the board
pygame.init()
board = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

#Draw grid circles
for col in range(NCOLUMNS):
    for row in range(NROWS):
        pygame.draw.rect(board, BLACK, (col * SQUARE, row * SQUARE, SQUARE, SQUARE))
        pygame.draw.circle(board, WHITE, (int(col * SQUARE + SQUARE / 2), int(row * SQUARE + SQUARE / 2)), RADIUS)
                        
pygame.display.update()

class Board:

    def __init__(self):
        self.grid = np.zeros((NROWS, NCOLUMNS))
        self.signed = 0
    
    def valid_column(self, column):
        """ 
        return True if the column is valid, so if it is not full.

        Parameters
        ----------
        column : int value, number of the choosen column
        """
        return self.grid[NROWS - 1][column] == 0
    
    def next_row(self, column):
        """ 
        return the next empty row on a choosen column.

        Parameters
        ----------
        column : int value, number of the choosen column
        """
        for row in range(NROWS):
            if self.grid[row][column] == 0: return row
    
    def print_figure(self):
        """ 
        print the circle in the choosen position.

        Parameters
        ----------
        column : int value, number of the choosen column
        """
        for col in range(NCOLUMNS):
            for row in range(NROWS):
                if self.grid[row][col] == 1:
                    pygame.draw.circle(board, YELLOW,  (int(col * SQUARE + SQUARE / 2), HEIGHT - int(row * SQUARE + SQUARE / 2)), RADIUS)
                elif self.grid[row][col] == 2:
                    pygame.draw.circle(board, RED,  (int(col * SQUARE + SQUARE / 2), HEIGHT -int(row * SQUARE + SQUARE / 2)), RADIUS)
        pygame.display.update()

    def sign(self, column, player):
        """ 
        sign the player into the choosen column on the next row.

        Parameters
        ----------
        column : int value, column coordinate of the choosen square
        player : int value, ID of the player (1 or 2)
        """
        if self.valid_column(column):
            row = self.next_row(column)
            self.grid[row][column] = player
            self.signed += 1

    def check_grid(self, win):
        """ 
        check if a player win the game, if win parameter is setted to True it also show the victory with a green line.

        Parameters
        ----------
        win : boolean value, show the victory with a green line.
        """
        for col in range(NCOLUMNS - 3):
            for row in range(NROWS):
                if self.grid[row][col] == self.grid[row][col + 1] == self.grid[row][col + 2] == self.grid[row][col + 3] != 0:
                    if win:
                        self.print_victory((row, col), (row, col + 3))
                    return self.grid[row][col]
        
        for row in range(NROWS - 3):
            for col in range(NCOLUMNS):
                if self.grid[row][col] == self.grid[row + 1][col] == self.grid[row + 2][col] == self.grid[row + 3][col] != 0:
                    if win: self.print_victory((row, col), (row + 3, col))
                    return self.grid[row][col]

        for row in range(NROWS - 3):
            for col in range(NCOLUMNS - 3):
                if self.grid[row][col] == self.grid[row + 1][col + 1] == self.grid[row + 2][col + 2] == self.grid[row + 3][col + 3] != 0:
                    if win: self.print_victory((row, col), (row + 3, col + 3))
                    return self.grid[row][col]
        
        for row in range(3, NROWS):
            for col in range(NCOLUMNS - 3):
                if self.grid[row][col] == self.grid[row - 1][col + 1] == self.grid[row - 2][col + 2] == self.grid[row - 3][col + 3] != 0:
                    if win: self.print_victory((row, col), (row - 3, col + 3))
                    return self.grid[row][col]
        
        if self.is_full(): return 0
    
    def is_full(self):
        """ 
        return True if the board is full, False otherwise.
        """
        if self.signed == NROWS * NCOLUMNS: return True
        return False 

    def free_columns(self):
        """ 
        return a list of the remain free columns.
        """
        return [i for i in range(NCOLUMNS) if self.valid_column(i)]
    
    def print_victory(self, start, end):
        """ 
        show the victory with a green line.

        Parameters
        ----------
        start : tuple of int, represent the position of the initial point of the green line.
        end : tuple of int, represent the position of the ended point of the green line.
        """
        pygame.draw.line(board, GREEN, (start[1] * SQUARE + SQUARE // 2, (5 - start[0]) * SQUARE + SQUARE // 2), (end[1] * SQUARE + SQUARE // 2, (5 - end[0]) * SQUARE + SQUARE // 2), 5)