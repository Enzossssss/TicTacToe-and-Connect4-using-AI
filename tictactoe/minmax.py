#Imported Libraries
import copy
from board import *

class MinMax:

    def __init__(self, player = 2, max_or_min = False):
        self.player = player
        self.max_or_min = max_or_min

    def minmax(self, board, max_or_min, alpha, beta):
        """ 
        Min-Max alghorithm with alpha-beta cuts.

        Parameters
        ----------
        board : object of type Board, that represents the board taken into consideration to execute the Min-Max alghorithm 
        max_or_min : boolean value, True if the player is maximize the values, False otherwise.
        alpha : int value, initial value of alpha
        beta : int value, initial value of beta
        """
        
        leaf = board.check_grid(False)
        
        if leaf == 1: return 1, None
        if leaf == 2: return -1, None
        if board.signed == 9: return 0, None

        if max_or_min:
            maxx = -100000
            move = None
            possible_position = board.free_position()

            for (r, c) in possible_position:
                tmp = copy.deepcopy(board)
                tmp.sign(r, c, 1)
                res = self.minmax(tmp, False, alpha, beta)[0]
                if res > maxx:
                    maxx = res
                    move = (r, c)
                alpha = max(maxx, alpha)
                if alpha >= beta:
                    break

            return maxx, move
        else:
            move = None
            minn = 10000
            possible_position = board.free_position()
            for (r, c) in possible_position:
                tmp = copy.deepcopy(board)
                tmp.sign(r, c, 2)
                res = self.minmax(tmp, True, alpha, beta)[0]
                if res < minn:
                    minn = res
                    move = (r, c)
                beta = min(minn, beta)
                if alpha >= beta:
                    break

            return minn, move