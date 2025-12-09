import pygame
from config import *
from ultilis import draw_text
from pontos import draw_modern_scoreboard

def draw_board(screen, board, scores, current_player, game_time):
    screen.fill(BG_COLOR)

    # Fundo do tabuleiro
    board_bg = pygame.Rect(BOARD_MARGIN - 10, -10, 620, 620)
    pygame.draw.rect(screen, (40, 40, 60), board_bg, border_radius=15)
    pygame.draw.rect(screen, (80, 80, 120), board_bg, 3, border_radius=15)

    # Linhas do tabuleiro
    _draw_grid_lines(screen)
    
    # Símbolos
    _draw_symbols(screen, board)

    # Placar
    draw_modern_scoreboard(screen, scores, current_player, game_time)

def _draw_grid_lines(screen):
    for i in range(BOARD_SIZE + 1):
        # Linhas verticais
        x = BOARD_MARGIN + i * CELL_SIZE
        pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, BOARD_SIZE * CELL_SIZE), 3)
        
        # Linhas horizontais
        y = i * CELL_SIZE
        pygame.draw.line(screen, LINE_COLOR, 
                        (BOARD_MARGIN, y), 
                        (BOARD_MARGIN + BOARD_SIZE * CELL_SIZE, y), 3)

def _draw_symbols(screen, board):
    font = pygame.font.SysFont("arial", CELL_SIZE // 2, bold=True)
    
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] != "":
                x_pos = BOARD_MARGIN + col * CELL_SIZE + CELL_SIZE//3
                y_pos = row * CELL_SIZE + CELL_SIZE//4
                
                if board[row][col] == "X":
                    shadow_color = (150, 30, 30)
                    main_color = PLAYER_X_COLOR
                else:
                    shadow_color = (30, 80, 150)
                    main_color = PLAYER_O_COLOR
                
                # Texto com sombra
                shadow_text = font.render(board[row][col], True, shadow_color)
                main_text = font.render(board[row][col], True, main_color)
                
                screen.blit(shadow_text, (x_pos + 2, y_pos + 2))
                screen.blit(main_text, (x_pos, y_pos))


