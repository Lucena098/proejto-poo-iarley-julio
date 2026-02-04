class Cell:
    def __init__(self):
        self.value = None


class SmallBoard:
    def __init__(self):
        self.cells = [[Cell() for _ in range(3)] for _ in range(3)]
        self.winner = None  # X, O, E (empate)

    def is_full(self):
        return all(self.cells[r][c].value for r in range(3) for c in range(3))

    def check_winner(self):
        lines = []

        lines.extend(self.cells)
        lines.extend([[self.cells[r][c] for r in range(3)] for c in range(3)])
        lines.append([self.cells[i][i] for i in range(3)])
        lines.append([self.cells[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0].value and all(cell.value == line[0].value for cell in line):
                self.winner = line[0].value
                return

        if self.is_full():
            self.winner = "E"


class BigBoard:
    def __init__(self):
        self.boards = [[SmallBoard() for _ in range(3)] for _ in range(3)]
        self.winner = None

    def check_winner(self):
        grid = [[b.winner for b in row] for row in self.boards]

        for i in range(3):
            if grid[i][0] and grid[i][0] != "E" and all(grid[i][j] == grid[i][0] for j in range(3)):
                self.winner = grid[i][0]
                return
            if grid[0][i] and grid[0][i] != "E" and all(grid[j][i] == grid[0][i] for j in range(3)):
                self.winner = grid[0][i]
                return

        if grid[0][0] and grid[0][0] != "E" and all(grid[i][i] == grid[0][0] for i in range(3)):
            self.winner = grid[0][0]
            return
        if grid[0][2] and grid[0][2] != "E" and all(grid[i][2 - i] == grid[0][2] for i in range(3)):
            self.winner = grid[0][2]
            return

        
        # ✅ EMPATE GLOBAL
        if all(b.winner for row in self.boards for b in row):
            self.winner = "E"



#button.py



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


#game.py 


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


            



#main.py


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





#menu.py


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





#rules.py


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

