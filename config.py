import pygame

# Tela
TAMANHO_TELA = 600
LINHAS = COLUNAS = 9
TAM_CELULA = TAMANHO_TELA // 9

# Cores
BRANCO = (240, 240, 240)
PRETO = (30, 30, 30)
AZUL = (70, 130, 255)
VERMELHO = (220, 80, 80)
VERDE = (80, 200, 120)

# Fonte
def get_fonte():
    return pygame.font.SysFont(None, 48)
