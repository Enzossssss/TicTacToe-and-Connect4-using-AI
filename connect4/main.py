#Imported Libraries
from match import *
import sys
import math

def main():

    match = Match()
    board = match.board
    ai = match.ai

    while True:

        pygame.display.update()

        if match.player == ai.player and not match.gameover:
            pygame.display.set_caption(GAME_NAME + ' - AI IS CHOOSING..')
            pygame.display.update()
            val, column = ai.min_max(board, 6, match.player, True, -10000000000, 10000000000)
            match.board.sign(column, match.player)
            match.board.print_figure()
            pygame.display.update()   
            match.change_player()
            match.game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and not match.gameover:
                    pygame.display.set_caption(GAME_NAME + ' - IT\'S NOT YOUR TURN, WAIT..')
                pygame.display.update()   
                        

        pygame.display.update()   

        if match.player != ai.player or match.gameover:
            pygame.display.set_caption(GAME_NAME + ' - YOUR TURN..')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and not match.gameover:

                    if match.player == match.human_player:
                        column = int(math.floor(event.pos[0]/SQUARE))
                        match.board.sign(column, match.player)
                        match.board.print_figure()
                        match.change_player()
                        match.game_over()
                        
        
        pygame.display.update()      

if __name__ == "__main__":
    main()