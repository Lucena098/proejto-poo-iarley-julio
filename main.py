import pygame
from config import *
from board import Board
from draw import desenhar_tabuleiro, desenhar_marcas, destacar_bloco

pygame.init()
tela = pygame.display.set_mode((TAMANHO_TELA, TAMANHO_TELA + 60))
pygame.display.set_caption("Jogo da Velha 9x9")

clock = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 28)

board = Board()
jogador = "X"
fim_de_jogo = False
bloco_vencedor = None
mensagem = "Vez do jogador: X"

rodando = True
while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                board = Board()
                jogador = "X"
                fim_de_jogo = False
                bloco_vencedor = None
                mensagem = "Vez do jogador: X"

        if evento.type == pygame.MOUSEBUTTONDOWN and not fim_de_jogo:
            x, y = pygame.mouse.get_pos()
            if y < TAMANHO_TELA:
                c = min(8, x // TAM_CELULA)
                l = min(8, y // TAM_CELULA)

                if board.definir(l, c, jogador):
                    vencedor, bloco = board.verificar_vitoria()
                    if vencedor:
                        fim_de_jogo = True
                        bloco_vencedor = bloco
                        mensagem = f"Jogador {vencedor} venceu! (R para reiniciar)"
                    else:
                        jogador = "O" if jogador == "X" else "X"
                        mensagem = f"Vez do jogador: {jogador}"

    tela.fill(BRANCO)

    desenhar_tabuleiro(tela)
    desenhar_marcas(tela, board)

    if bloco_vencedor:
        destacar_bloco(tela, bloco_vencedor[0], bloco_vencedor[1])

    texto = fonte.render(mensagem, True, PRETO)
    tela.blit(texto, (10, TAMANHO_TELA + 15))

    pygame.display.update()

pygame.quit()
