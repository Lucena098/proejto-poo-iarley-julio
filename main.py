import pygame
import sys
from config import *
from game import Game
from draw import *
from utils import pos_para_celula

pygame.init()
tela = pygame.display.set_mode((TAMANHO_TELA, TAMANHO_TELA))
pygame.display.set_caption("Jogo da Velha 2")

clock = pygame.time.Clock()
game = Game()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            linha, coluna = pos_para_celula(evento.pos, TAM_CELULA)
            game.jogar(linha, coluna)

    desenhar_tabuleiro(tela)
    desenhar_marcas(tela, game.board)

    pygame.display.update()
    clock.tick(60)
