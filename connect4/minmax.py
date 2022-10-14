#Imported Libraries
import copy
import random
from constants import *

class MinMax:

    def __init__(self, player = 2):
        self.player = player

    def other_player(self, player):
        """ 
        return the other player with respect to the current.

        Parameters
        ----------
        player : int value, ID of the player.
        """
        return player % 2 + 1

    def evaluate_positions(self, board, player):
        """ 
        evaluate a single position.

        Parameters
        ----------
        board : object of type Board, that represents the board taken into consideration to execute the Min-Max alghorithm.
        player : int value, ID of the player.
        """
        score = 0
        score += [int(i) for i in list(board.grid[:, NCOLUMNS // 2])].count(player) * 3

        for row in range(NROWS):
            row_elements = [int(i) for i in list(board.grid[row, :])]
            for col in range(NCOLUMNS - 3):
                elements = row_elements[col: col + 4]
                score += self.give_evaluation(elements, player)
                
        for col in range(NCOLUMNS):
            col_elements = [int(i) for i in list(board.grid[:, col])]
            for row in range(NROWS - 3):
                elements = col_elements[row: row + 4]
                score += self.give_evaluation(elements, player)
                
        for row in range(NROWS - 3):
            for col in range(NCOLUMNS - 3):
                elements = [board.grid[row + i, col + i] for i in range(4)]
                score += self.give_evaluation(elements, player)
                
        for row in range(NROWS - 3):
            for col in range(NCOLUMNS - 3):
                elements = [board.grid[row + 3 - i, col + i] for i in range(4)]
                score += self.give_evaluation(elements, player)
        
        return score

    def give_evaluation(self, elements, player):
        """ 
        evaluate some piece disposition.

        Parameters
        ----------
        elements : list of four positio taken in consideration.
        player : int value, ID of the player.
        """
        score = 0
        other_player = self.other_player(player)
        if elements.count(player) == 4:
            score += 100
        elif elements.count(player) == 3 and elements.count(0) == 1:
            score += 5
        elif elements.count(player) == 2 and elements.count(0) == 2:
            score += 2
        
        if elements.count(other_player) == 3 and elements.count(0) == 1:
            score -= 4

        return score
    
    def min_max(self, board, depth, player, maximizing, alpha, beta):
        """ 
        Min-Max alghorithm with alpha-beta cuts.

        Parameters
        ----------
        board : object of type Board, that represents the board taken into consideration to execute the Min-Max alghorithm.
        depth : int value, represents the max depth that we want to reach.
        player : int value, ID of the player.
        maximizing : boolean value, True if the player is maximize the values, False otherwise.
        alpha : int value, initial value of alpha
        beta : int value, initial value of beta
        """
        freecols = board.free_columns()
        if (board.check_grid(False) != None or board.is_full() or depth == 0):
            if board.check_grid(False) != None:
                if board.check_grid(False) == player:
                    return 1000000, None
                elif board.check_grid(False) == self.other_player(player):
                    return -1000000, None
                else:
                    return 0, None
            else:
                return self.evaluate_positions(board, player), None
        if maximizing:
            maxx = -1000000000
            best_pos = random.choice(freecols)
            for col in freecols:
                tmp = copy.deepcopy(board)
                tmp.sign(col, player)
                evaluation = self.min_max(tmp, depth - 1, player, False, alpha, beta)[0]
                if evaluation > maxx:
                    maxx = evaluation
                    best_pos = col
                alpha = max(maxx, alpha)
                if alpha >= beta:
                    break
            return maxx, best_pos
        else:
            minn = 1000000000
            best_pos = random.choice(freecols)
            for col in freecols:
                tmp = copy.deepcopy(board)
                tmp.sign(col, self.other_player(player))
                evaluation = self.min_max(tmp, depth - 1, player, True, alpha, beta)[0]
                if evaluation < minn:
                    minn = evaluation
                    best_pos = col
                beta = min(minn, beta)
                if alpha >= beta:
                    break
            return minn, best_pos