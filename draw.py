import pygame
from config import *

def desenhar_tabuleiro(tela):
    tela.fill(BRANCO)

    for i in range(10):
        espessura = 4 if i % 3 == 0 else 1
        pygame.draw.line(
            tela, PRETO,
            (0, i * TAM_CELULA),
            (TAMANHO_TELA, i * TAM_CELULA),
            espessura
        )
        pygame.draw.line(
            tela, PRETO,
            (i * TAM_CELULA, 0),
            (i * TAM_CELULA, TAMANHO_TELA),
            espessura
        )

def desenhar_marcas(tela, board):
    fonte = get_fonte()

    for linha in range(9):
        for coluna in range(9):
            marca = board.obter(linha, coluna)
            if marca != " ":
                cor = AZUL if marca == "X" else VERMELHO
                texto = fonte.render(marca, True, cor)

                x = coluna * TAM_CELULA + TAM_CELULA // 2
                y = linha * TAM_CELULA + TAM_CELULA // 2
                tela.blit(texto, texto.get_rect(center=(x, y)))

