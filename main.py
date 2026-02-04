import pygame
pygame.init()
import sys
from menu import Menu
from rules import RulesScreen
from game import GameScreen


WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha 2")
CLOCK = pygame.time.Clock()

class App:
    def __init__(self):
        self.state = "menu"
        self.menu = Menu(self)
        self.rules = RulesScreen(self)
        self.game = GameScreen()

    def run(self):
        while True:
            CLOCK.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.state == "menu":
                    self.menu.handle_event(event)
                elif self.state == "rules":
                    self.rules.handle_event(event)
                elif self.state == "game" and event.type == pygame.MOUSEBUTTONDOWN:
                    result = self.game.click(pygame.mouse.get_pos())
                    if result == "menu":
                        self.state = "menu"
                        self.game = GameScreen()  # reseta o jogo


            if self.state == "menu":
                self.menu.draw(SCREEN)
            elif self.state == "rules":
                self.rules.draw(SCREEN)
            elif self.state == "game":
                self.game.draw(SCREEN)

            pygame.display.flip()

if __name__ == "__main__":
    App().run()

