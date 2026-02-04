import pygame
from board import Board
from settings import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()
        self.player = "X"

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.board.play(*event.pos, self.player):
                self.player = "O" if self.player == "X" else "X"

    def update(self):
        pass

    def draw_score(self):
        pygame.draw.rect(self.screen, SCORE_BG, (0, 0, WIDTH, SCORE_HEIGHT))
        text = SCORE_FONT.render(
            f"X: {self.board.score['X']}   O: {self.board.score['O']}",
            True,
            LINE_COLOR
        )
        self.screen.blit(text, text.get_rect(center=(WIDTH//2, SCORE_HEIGHT//2)))
        pygame.draw.line(
            self.screen, LINE_COLOR,
            (0, SCORE_HEIGHT), (WIDTH, SCORE_HEIGHT), 4
        )

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.draw_score()
        self.board.draw(self.screen)


