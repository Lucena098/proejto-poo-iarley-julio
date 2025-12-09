import pygame
import math
from config import *
from ultilis import draw_text

def draw_modern_scoreboard(screen, scores, current_player, game_time):
    scoreboard_y = 620
    scoreboard_height = 250
    
    # Fundo do placar
    scoreboard_rect = pygame.Rect(50, scoreboard_y, SCREEN_WIDTH - 100, scoreboard_height)
    pygame.draw.rect(screen, SCORE_BG_COLOR, scoreboard_rect, border_radius=20)
    pygame.draw.rect(screen, SCORE_BORDER_COLOR, scoreboard_rect, 4, border_radius=20)
    
    # Divisória central
    pygame.draw.line(screen, SCORE_BORDER_COLOR, 
                    (SCREEN_WIDTH // 2, scoreboard_y + 20),
                    (SCREEN_WIDTH // 2, scoreboard_y + scoreboard_height - 20), 3)
    
    # Desenhar jogadores
    _draw_player_section(screen, "X", SCREEN_WIDTH // 4, scoreboard_y, scores['X'], current_player)
    _draw_player_section(screen, "O", 3 * SCREEN_WIDTH // 4, scoreboard_y, scores['O'], current_player)
    
    # Informações centrais
    _draw_center_info(screen, scores, game_time, scoreboard_y)

def _draw_player_section(screen, player, x_pos, scoreboard_y, score, current_player):
    # Cabeçalho do jogador
    color = PLAYER_X_COLOR if player == "X" else PLAYER_O_COLOR
    highlight_color = (255, 150, 150) if player == "X" else (150, 200, 255)
    
    player_bg = pygame.Rect(x_pos - 120, scoreboard_y + 30, 240, 50)
    pygame.draw.rect(screen, color, player_bg, border_radius=12)
    pygame.draw.rect(screen, highlight_color, player_bg, 3, border_radius=12)
    draw_text(screen, f"JOGADOR {player}", 28, x_pos, scoreboard_y + 55, WHITE)
    
    # Pontuação
    score_y = scoreboard_y + 130
    draw_text(screen, str(score), 72, x_pos, score_y, color)
    draw_text(screen, "PONTOS", 22, x_pos, score_y + 50, (200, 200, 200))
    
    # Indicador "SUA VEZ!"
    if current_player == player:
        _draw_turn_indicator(screen, x_pos, scoreboard_y + 190)

def _draw_turn_indicator(screen, x, y):
    # Efeito de pulso
    pulse = abs(pygame.time.get_ticks() % 1000 - 500) / 500
    pulse_size = 20 + int(pulse * 10)
    
    # Círculo externo pulsante
    for r in range(pulse_size, pulse_size - 8, -2):
        pygame.draw.circle(screen, (255, 255, 0), (x, y), r, 3)
    
    # Círculo principal
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 15)
    pygame.draw.circle(screen, (255, 200, 0), (x, y), 12)
    
    # Efeito de raios brilhantes
    for angle in range(0, 360, 45):
        rad = angle * math.pi / 180
        start_x = x + 18 * math.cos(rad)
        start_y = y + 18 * math.sin(rad)
        end_x = x + 25 * math.cos(rad)
        end_y = y + 25 * math.sin(rad)
        pygame.draw.line(screen, (255, 255, 100), (start_x, start_y), (end_x, end_y), 3)
    
    # Fundo para o texto
    text_bg = pygame.Rect(x - 60, y + 25, 120, 30)
    pygame.draw.rect(screen, (255, 200, 0), text_bg, border_radius=8)
    pygame.draw.rect(screen, (255, 255, 100), text_bg, 2, border_radius=8)
    
    # Texto
    draw_text(screen, "SUA VEZ!", 22, x, y + 40, (50, 30, 0))
    
    # Partículas ao redor
    _draw_particles(screen, x, y)

def _draw_particles(screen, x, y):
    for i in range(6):
        angle = (pygame.time.get_ticks() / 100 + i * 60) % 360
        rad = angle * math.pi / 180
        dist = 35 + math.sin(pygame.time.get_ticks() / 200 + i) * 5
        part_x = x + dist * math.cos(rad)
        part_y = y + dist * math.sin(rad)
        pygame.draw.circle(screen, (255, 255, 100), (int(part_x), int(part_y)), 3)

def _draw_center_info(screen, scores, game_time, scoreboard_y):
    center_x = SCREEN_WIDTH // 2
    
    # Tempo de jogo
    time_bg = pygame.Rect(center_x - 100, scoreboard_y + 30, 200, 40)
    pygame.draw.rect(screen, (60, 60, 90), time_bg, border_radius=10)
    draw_text(screen, "TEMPO", 20, center_x, scoreboard_y + 50, (200, 200, 255))
    draw_text(screen, game_time, 28, center_x, scoreboard_y + 80, WHITE)
    
    # Diferença de pontos
    diff = abs(scores['X'] - scores['O'])
    if scores['X'] > scores['O']:
        diff_text = f"X +{diff}"
        diff_color = PLAYER_X_COLOR
    elif scores['O'] > scores['X']:
        diff_text = f"O +{diff}"
        diff_color = PLAYER_O_COLOR
    else:
        diff_text = "EMPATE"
        diff_color = WHITE
    
    diff_bg = pygame.Rect(center_x - 80, scoreboard_y + 110, 160, 35)
    pygame.draw.rect(screen, (60, 60, 90), diff_bg, border_radius=8)
    draw_text(screen, "DIFERENÇA", 18, center_x, scoreboard_y + 128, (200, 200, 255))
    draw_text(screen, diff_text, 26, center_x, scoreboard_y + 160, diff_color)
    
    # Barra de progresso
    _draw_progress_bar(screen, scores, center_x, scoreboard_y)

def _draw_progress_bar(screen, scores, center_x, scoreboard_y):
    total_points = scores['X'] + scores['O']
    if total_points > 0:
        x_percentage = (scores['X'] / total_points) * 100
        
        bar_width = 300
        bar_height = 20
        bar_x = center_x - bar_width // 2
        bar_y = scoreboard_y + 220
        
        # Fundo da barra
        pygame.draw.rect(screen, (50, 50, 70), (bar_x, bar_y, bar_width, bar_height), border_radius=10)
        pygame.draw.rect(screen, (80, 80, 100), (bar_x, bar_y, bar_width, bar_height), 2, border_radius=10)
        
        # Preenchimento X
        if scores['X'] > 0:
            x_width = int((x_percentage / 100) * bar_width)
            pygame.draw.rect(screen, PLAYER_X_COLOR, (bar_x, bar_y, x_width, bar_height), border_radius=10)
        
        # Preenchimento O
        if scores['O'] > 0:
            o_width = int(((100 - x_percentage) / 100) * bar_width)
            pygame.draw.rect(screen, PLAYER_O_COLOR, (bar_x + bar_width - o_width, bar_y, o_width, bar_height), border_radius=10)
        
        # Marcador do meio
        pygame.draw.line(screen, WHITE, (center_x, bar_y - 5), (center_x, bar_y + bar_height + 5), 3)


