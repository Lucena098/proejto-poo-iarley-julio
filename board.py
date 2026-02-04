from miniboard import MiniBoard
from settings import *

class Board:
    def __init__(self):
        self.boards = [[MiniBoard() for _ in range(3)] for _ in range(3)]
        self.active_board = (1, 1)
        self.score = {"X": 0, "O": 0}
        self.game_over = False

    def draw(self, screen):
        offset = SCORE_HEIGHT

        for br in range(3):
            for bc in range(3):
                active = (
                    not self.game_over and
                    (self.active_board is None or (br, bc) == self.active_board)
                )
                self.boards[br][bc].draw(screen, br, bc, active, offset)

        for i in range(1, 3):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, offset + i * 3 * CELL_SIZE),
                (CELL_SIZE * 9, offset + i * 3 * CELL_SIZE),
                6
            )
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * 3 * CELL_SIZE, offset),
                (i * 3 * CELL_SIZE, offset + CELL_SIZE * 9),
                6
            )

    def play(self, x, y, player):
        y -= SCORE_HEIGHT
        if y < 0 or y >= BOARD_HEIGHT:
            return False

        col = x // CELL_SIZE
        row = y // CELL_SIZE

        br, bc = row // 3, col // 3
        cr, cc = row % 3, col % 3

        if self.active_board and (br, bc) != self.active_board:
            return False

        board = self.boards[br][bc]

        if board.play(cr, cc, player):
            if board.winner:
                self.score[player] += 1

            next_board = (cr, cc)
            if self.boards[next_board[0]][next_board[1]].winner:
                self.active_board = None
            else:
                self.active_board = next_board

            return True

        return False



