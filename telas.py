import pygame
from config import *
from ultilis import draw_text, draw_button
from datetime import datetime

def main_menu(screen):
    menu_running = True
    
    while menu_running:
        screen.fill(MENU_BG_COLOR)
        
        # Título do jogo
        draw_text(screen, "JOGO DA VELHA 9x9", 56, SCREEN_WIDTH//2, 120, WHITE)
        draw_text(screen, "PLACAR SUPREMO", 36, SCREEN_WIDTH//2, 180, (255, 215, 0))
        
        # Botões do menu
        play_button = draw_button(screen, "JOGAR", SCREEN_WIDTH//2 - 150, 280, 300, 70)
        scores_button = draw_button(screen, "PLACARES", SCREEN_WIDTH//2 - 150, 370, 300, 70)
        quit_button = draw_button(screen, "SAIR", SCREEN_WIDTH//2 - 150, 460, 300, 70)
        
        # Preview do placar
        _draw_score_preview(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return "play"
                elif scores_button.collidepoint(event.pos):
                    return "scores"
                elif quit_button.collidepoint(event.pos):
                    return "quit"
    
    return "quit"

def _draw_score_preview(screen):
    preview_rect = pygame.Rect(80, 550, SCREEN_WIDTH - 160, 200)
    pygame.draw.rect(screen, SCORE_BG_COLOR, preview_rect, border_radius=20)
    pygame.draw.rect(screen, SCORE_BORDER_COLOR, preview_rect, 4, border_radius=20)
    
    draw_text(screen, "PLACAR INTERATIVO", 28, SCREEN_WIDTH//2, 580, (255, 215, 0))
    draw_text(screen, "• Tempo real • Progresso visual • Destaques animados", 20, SCREEN_WIDTH//2, 620, WHITE)
    
    # Mini placar
    draw_text(screen, "X  8", 36, SCREEN_WIDTH//2 - 100, 680, PLAYER_X_COLOR)
    draw_text(screen, "VS", 24, SCREEN_WIDTH//2, 680, WHITE)
    draw_text(screen, "5  O", 36, SCREEN_WIDTH//2 + 100, 680, PLAYER_O_COLOR)

def scores_screen(screen, scores_history):
    scores_running = True
    
    while scores_running:
        screen.fill(MENU_BG_COLOR)
        
        draw_text(screen, "HISTÓRICO DE PARTIDAS", 36, SCREEN_WIDTH//2, 60, WHITE)
        
        if not scores_history:
            draw_text(screen, "Nenhuma partida registrada ainda", 24, SCREEN_WIDTH//2, 300, (200, 200, 200))
        else:
            y_pos = 120
            for i, score in enumerate(scores_history[-8:]):
                draw_text(screen, f"Partida {i+1}: X={score['X']} | O={score['O']} | {score['date']}", 
                         20, SCREEN_WIDTH//2, y_pos, WHITE)
                y_pos += 40
        
        back_button = draw_button(screen, "VOLTAR", SCREEN_WIDTH//2 - 75, SCREEN_HEIGHT - 100, 150, 50)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    scores_running = False
    
    return True
