
import pygame
from board import BigBoard

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (70, 130, 180)
RED = (200, 50, 50)

WIDTH, HEIGHT = 800, 600


class GameScreen:
    def __init__(self):
        self.board = BigBoard()
        self.current_player = "X"
        self.active_board = None  # (linha, coluna)
        self.winner = None

        pygame.font.init()
        self.font = pygame.font.SysFont(None, 36)
        self.big_font = pygame.font.SysFont(None, 120)

        # Layout
        self.small_size = 140
        self.cell_size = self.small_size // 3
        self.gap = 15

        total = self.small_size * 3 + self.gap * 2
        self.start_x = (WIDTH - total) // 2
        self.start_y = (HEIGHT - total) // 2

        self.btn_restart = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2, 180, 50)
        self.btn_menu = pygame.Rect(WIDTH // 2 + 20, HEIGHT // 2, 140, 50)


        self.btn_font = pygame.font.SysFont(None, 28)


    # -------------------------------------------------

    def click(self, pos):
        if self.winner:
            if self.btn_restart.collidepoint(pos):
                self.__init__()
            elif self.btn_menu.collidepoint(pos):
                return "menu"
            return None

        mx, my = pos

        for br in range(3):
            for bc in range(3):

                if self.active_board and self.active_board != (br, bc):
                    continue

                sb = self.board.boards[br][bc]
                if sb.winner:
                    continue

                bx = self.start_x + bc * (self.small_size + self.gap)
                by = self.start_y + br * (self.small_size + self.gap)

                if not pygame.Rect(bx, by, self.small_size, self.small_size).collidepoint(mx, my):
                    continue

                c = (mx - bx) // self.cell_size
                r = (my - by) // self.cell_size

                if sb.cells[r][c].value:
                    return None

                sb.cells[r][c].value = self.current_player
                sb.check_winner()

                # define próximo tabuleiro
                if sb.winner == "E":
                    self.active_board = None
                else:
                    self.active_board = (r, c)
                    if self.board.boards[r][c].winner:
                        self.active_board = None

                self.board.check_winner()
                if self.board.winner:
                    self.winner = self.board.winner
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
                return None

    # -------------------------------------------------

    def draw(self, screen):
        screen.fill(GRAY)

        for br in range(3):
            for bc in range(3):
                sb = self.board.boards[br][bc]

                bx = self.start_x + bc * (self.small_size + self.gap)
                by = self.start_y + br * (self.small_size + self.gap)

                # destaque do tabuleiro ativo
                if self.active_board is None:
                    if not sb.winner:
                        pygame.draw.rect(
                            screen, BLUE,
                            (bx - 4, by - 4, self.small_size + 8, self.small_size + 8),
                            3
                        )
                elif self.active_board == (br, bc):
                    pygame.draw.rect(
                        screen, BLUE,
                        (bx - 4, by - 4, self.small_size + 8, self.small_size + 8),
                        4
                    )

                # borda do tabuleiro pequeno
                pygame.draw.rect(screen, BLACK, (bx, by, self.small_size, self.small_size), 3)

                # linhas internas 3x3
                for i in range(1, 3):
                    pygame.draw.line(
                        screen, BLACK,
                        (bx + i * self.cell_size, by),
                        (bx + i * self.cell_size, by + self.small_size),
                        1
                    )
                    pygame.draw.line(
                        screen, BLACK,
                        (bx, by + i * self.cell_size),
                        (bx + self.small_size, by + i * self.cell_size),
                        1
                    )

                # X e O pequenos
                for r in range(3):
                    for c in range(3):
                        cell = sb.cells[r][c]
                        if cell.value:
                            txt = self.font.render(cell.value, True, BLACK)
                            rect = txt.get_rect(
                                center=(
                                    bx + c * self.cell_size + self.cell_size // 2,
                                    by + r * self.cell_size + self.cell_size // 2
                                )
                            )
                            screen.blit(txt, rect)

        # símbolo grande (X, O ou E) — SEMPRE POR ÚLTIMO
                if sb.winner:
                    color = RED if sb.winner in ("X", "O") else BLACK
                    big = self.big_font.render(sb.winner, True, color)
                    rect = big.get_rect(
                        center=(
                            bx + self.small_size // 2,
                            by + self.small_size // 2
                        )
                    )
                    screen.blit(big, rect)



        self.draw_ui(screen)

    # -------------------------------------------------

    def draw_ui(self, screen):
        turn = self.font.render(f"Turno: {self.current_player}", True, BLACK)
        screen.blit(turn, (20, 20))

        if self.winner:

            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(140)  # transparência (0–255)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))


            if self.winner == "E":
                msg = "Empate!"
            else:
                msg = f"O jogador {self.winner} venceu!"

            txt = self.font.render(msg, True, RED)
            screen.blit(txt, txt.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))




            pygame.draw.rect(screen, BLUE, self.btn_restart)
            pygame.draw.rect(screen, BLUE, self.btn_menu)

            txt_restart = self.btn_font.render("Jogar Novamente", True, WHITE)
            txt_menu = self.btn_font.render("Menu", True, WHITE)

            screen.blit(txt_restart, txt_restart.get_rect(center=self.btn_restart.center))
            screen.blit(txt_menu, txt_menu.get_rect(center=self.btn_menu.center))
