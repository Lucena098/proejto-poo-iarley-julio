import pygame
import math
from config import *

def draw_text(surface, text, size, x, y, color=WHITE, centered=True):
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if centered:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)
    return text_rect

def draw_button(surface, text, x, y, width, height, color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR):
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(x, y, width, height)
    
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(surface, hover_color, button_rect, border_radius=15)
    else:
        pygame.draw.rect(surface, color, button_rect, border_radius=15)
    
    pygame.draw.rect(surface, WHITE, button_rect, 3, border_radius=15)
    draw_text(surface, text, 32, x + width//2, y + height//2)
    
    return button_rect

def format_game_time(start_time):
    elapsed = pygame.time.get_ticks() - start_time
    seconds = elapsed // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


