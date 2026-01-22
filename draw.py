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
            valor = board.obter(linha, coluna)
            if valor != " ":
                texto = fonte.render(valor, True, AZUL)
                x = coluna * TAM_CELULA + TAM_CELULA // 2
                y = linha * TAM_CELULA + TAM_CELULA // 2
                tela.blit(texto, texto.get_rect(center=(x, y)))

def destacar_bloco(tela, bl, bc):
    rect = pygame.Rect(
        bc * TAM_CELULA,
        bl * TAM_CELULA,
        TAM_CELULA * 3,
        TAM_CELULA * 3
    )
    pygame.draw.rect(tela, (0, 200, 0), rect, 4)
