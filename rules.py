
import pygame
from button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600
FONT = pygame.font.SysFont(None, 30)

class RulesScreen:
    def __init__(self, game):
        self.game = game
        self.back = Button("Voltar", (WIDTH//2, 520), self.go_back)

    def go_back(self):
        self.game.state = "menu"

    def draw(self, screen):
        screen.fill(BLACK)

        rules = [
            "Jogo da Velha 2 (Ultimate)",
            "",
            "- Cada jogada define o tabuleiro da próxima jogada",
            "- Se o tabuleiro estiver ganho ou empatado, pode jogar em qualquer um",
            "- Ganhar um tabuleiro pequeno marca o tabuleiro grande",
            "- Ganha quem fizer 3 tabuleiros em linha ou diagonal"
        ]

        for i, line in enumerate(rules):
            txt = FONT.render(line, True, WHITE)
            screen.blit(txt, (60, 120 + i * 35))

        self.back.draw(screen, pygame.mouse.get_pos())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.back.click(pygame.mouse.get_pos())
