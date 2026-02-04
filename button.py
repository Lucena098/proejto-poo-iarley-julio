
import pygame

WHITE = (255, 255, 255)
BLUE = (70, 130, 180)

class Button:
    def __init__(self, text, pos, action):
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont(None, 48)
        self.label = self.font.render(text, True, WHITE)
        self.rect = self.label.get_rect(center=pos)

    def draw(self, screen, mouse):
        color = BLUE if self.rect.collidepoint(mouse) else WHITE
        label = self.font.render(self.text, True, color)
        screen.blit(label, self.rect)

    def click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.action()
