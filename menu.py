
import pygame
from button import Button

WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Menu:
    def __init__(self, game):
        self.game = game
        self.buttons = [
            Button("Jogar", (WIDTH//2, 250), self.start),
            Button("Regras", (WIDTH//2, 320), self.rules),
            Button("Sair", (WIDTH//2, 390), self.exit)
        ]

    def start(self):
        self.game.state = "game"

    def rules(self):
        self.game.state = "rules"

    def exit(self):
        pygame.quit()
        exit()

    def draw(self, screen):
        screen.fill(BLACK)
        title = pygame.font.SysFont(None, 56).render("JOGO DA VELHA 2", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))

        mouse = pygame.mouse.get_pos()
        for b in self.buttons:
            b.draw(screen, mouse)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in self.buttons:
                b.click(pygame.mouse.get_pos())
