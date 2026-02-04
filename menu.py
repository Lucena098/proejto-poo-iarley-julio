import pygame
import sys
from settings import WIDTH, HEIGHT, BG_COLOR, LINE_COLOR, SCORE_BG

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont("arial", 56, bold=True)
        self.button_font = pygame.font.SysFont("arial", 36, bold=True)

        self.play_rect = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 - 30, 240, 60)
        self.exit_rect = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 + 50, 240, 60)

    def draw(self):
        self.screen.fill(BG_COLOR)

        # título
        title = self.title_font.render("JOGO DA VELHA 2", True, LINE_COLOR)
        title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//3))
        self.screen.blit(title, title_rect)

        # botão jogar
        pygame.draw.rect(self.screen, SCORE_BG, self.play_rect, border_radius=10)
        pygame.draw.rect(self.screen, LINE_COLOR, self.play_rect, 3, border_radius=10)
        play_text = self.button_font.render("JOGAR", True, LINE_COLOR)
        self.screen.blit(play_text, play_text.get_rect(center=self.play_rect.center))

        # botão sair
        pygame.draw.rect(self.screen, SCORE_BG, self.exit_rect, border_radius=10)
        pygame.draw.rect(self.screen, LINE_COLOR, self.exit_rect, 3, border_radius=10)
        exit_text = self.button_font.render("SAIR", True, LINE_COLOR)
        self.screen.blit(exit_text, exit_text.get_rect(center=self.exit_rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_rect.collidepoint(event.pos):
                return "play"
            if self.exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

        return None
