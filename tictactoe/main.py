#Imported Libraries
import pygame
import sys
from constants import *
from board import *
from match import Match

def main():

    match = Match()
    board = match.board
    ai = match.ai
    
    while True:

        if match.player == ai.player and match.gameover:
            pygame.display.set_caption(GAME_NAME + ' - AI IS CHOOSING..')
            pygame.display.update()
            val, coords = ai.minmax(board, ai.max_or_min, -10000000000, 10000000000)
            board.sign(coords[0], coords[1], ai.player)
            match.print_figure(coords[0], coords[1])
            match.change_player()

            if match.game_over(): match.gameover = False
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.display.set_caption(GAME_NAME + ' - IT\'S NOT YOUR TURN, WAIT..')
                pygame.display.update()  

        if match.player != ai.player or not match.gameover:
            pygame.display.set_caption(GAME_NAME + ' - YOUR TURN..')
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:

                    row = event.pos[1] // SQUARE_SIZE
                    column = event.pos[0] // SQUARE_SIZE

                    if board.its_empty(row, column) and match.gameover:
                        board.sign(row, column, match.player)
                        match.print_figure(row, column)
                        match.change_player()

                        if match.game_over(): 
                            match.gameover = False

        pygame.display.update()

if __name__ == "__main__":
    main()