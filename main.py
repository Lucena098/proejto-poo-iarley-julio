import pygame
import sys
from datetime import datetime

from config import *
from ultilis import format_game_time
from render_borda import draw_board
from logica_jogo import check_new_triples, is_board_full
from telas import main_menu, scores_screen

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jogo da Velha 9x9 - PLACAR SUPREMO")
        self.scores_history = []
    
    def run(self):
        while True:
            menu_choice = main_menu(self.screen)
            
            if menu_choice == "play":
                self.game_loop()
            elif menu_choice == "scores":
                scores_screen(self.screen, self.scores_history)
            elif menu_choice == "quit":
                pygame.quit()
                sys.exit()
    
    def game_loop(self):
        board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        current_player = "X"
        scores = {"X": 0, "O": 0}
        scored_positions = []
        start_time = pygame.time.get_ticks()

        running = True
        while running:
            game_time = format_game_time(start_time)
            draw_board(self.screen, board, scores, current_player, game_time)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    col = (x - BOARD_MARGIN) // CELL_SIZE
                    row = y // CELL_SIZE

                    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                        if board[row][col] == "":
                            board[row][col] = current_player
                            gained, new_scored = check_new_triples(board, current_player, scored_positions)
                            scores[current_player] += gained
                            scored_positions.extend(new_scored)
                            
                            if is_board_full(board):
                                self.scores_history.append({
                                    'X': scores['X'],
                                    'O': scores['O'],
                                    'date': datetime.now().strftime("%H:%M %d/%m")
                                })
                                return
                            
                            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    game = Game()
    game.run()

