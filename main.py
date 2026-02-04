import pygame
import sys
from settings import


# IMPORTAÇÃO EXPLÍCITA (SEM *)
from settings import (
    WIDTH, HEIGHT,
    BG_COLOR, LINE_COLOR,
    SCORE_BG
)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha 2")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 48, bold=True)

MENU = "menu"
PLAYING = "playing"
state = MENU

# botões
play_rect = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 - 40, 240, 70)
exit_rect = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 + 50, 240, 70)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == MENU and event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                print("JOGAR clicado")  # debug
                state = PLAYING
            if exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    screen.fill(BG_COLOR)

    if state == MENU:
        title = font.render("JOGO DA VELHA 2", True, LINE_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//3)))

        pygame.draw.rect(screen, SCORE_BG, play_rect, border_radius=12)
        pygame.draw.rect(screen, LINE_COLOR, play_rect, 3, border_radius=12)
        screen.blit(
            font.render("JOGAR", True, LINE_COLOR),
            font.render("JOGAR", True, LINE_COLOR).get_rect(center=play_rect.center)
        )

        pygame.draw.rect(screen, SCORE_BG, exit_rect, border_radius=12)
        pygame.draw.rect(screen, LINE_COLOR, exit_rect, 3, border_radius=12)
        screen.blit(
            font.render("SAIR", True, LINE_COLOR),
            font.render("SAIR", True, LINE_COLOR).get_rect(center=exit_rect.center)
        )

    pygame.display.flip()
    clock.tick(60)


