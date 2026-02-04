import pygame
from settings import CELL_SIZE, LINE_COLOR, FONT, BIG_FONT, X_COLOR, O_COLOR, ACTIVE_COLOR

class MiniBoard:
    def __init__(self):
        self.grid = [[None]*3 for _ in range(3)]
        self.winner = None

    def draw(self, screen, br, bc, active, offset):
        x0 = bc * 3 * CELL_SIZE
        y0 = br * 3 * CELL_SIZE + offset

        if active:
            pygame.draw.rect(
                screen,
                ACTIVE_COLOR,
                (x0, y0, 3*CELL_SIZE, 3*CELL_SIZE)
            )

        for i in range(1, 3):
            pygame.draw.line(
                screen, LINE_COLOR,
                (x0 + i*CELL_SIZE, y0),
                (x0 + i*CELL_SIZE, y0 + 3*CELL_SIZE), 2
            )
            pygame.draw.line(
                screen, LINE_COLOR,
                (x0, y0 + i*CELL_SIZE),
                (x0 + 3*CELL_SIZE, y0 + i*CELL_SIZE), 2
            )

        if self.winner:
            color = X_COLOR if self.winner == "X" else O_COLOR
            text = BIG_FONT.render(self.winner, True, color)
            rect = text.get_rect(center=(x0 + 1.5*CELL_SIZE, y0 + 1.5*CELL_SIZE))
            screen.blit(text, rect)
            return

        for r in range(3):
            for c in range(3):
                if self.grid[r][c]:
                    color = X_COLOR if self.grid[r][c] == "X" else O_COLOR
                    text = FONT.render(self.grid[r][c], True, color)
                    rect = text.get_rect(
                        center=(x0 + c*CELL_SIZE + CELL_SIZE//2,
                                y0 + r*CELL_SIZE + CELL_SIZE//2)
                    )
                    screen.blit(text, rect)

    def play(self, r, c, player):
        if self.grid[r][c] or self.winner:
            return False

        self.grid[r][c] = player
        self.check_winner(player)
        return True

    def check_winner(self, p):
        for i in range(3):
            if all(self.grid[i][c] == p for c in range(3)) or \
               all(self.grid[r][i] == p for r in range(3)):
                self.winner = p

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == p:
            self.winner = p
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == p:
            self.winner = p
