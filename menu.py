import pygame
from config import *

def mostrar_menu(tela):
    fonte_titulo = pygame.font.SysFont("arial", 48)
    fonte_botao = pygame.font.SysFont("arial", 32)

    botao_jogar = pygame.Rect(300, 300, 200, 50)
    botao_sair = pygame.Rect(300, 370, 200, 50)

    while True:
        tela.fill(BRANCO)

        titulo = fonte_titulo.render("Jogo da Velha 9x9", True, PRETO)
        tela.blit(titulo, titulo.get_rect(center=(TAMANHO_TELA // 2, 200)))

        pygame.draw.rect(tela, PRETO, botao_jogar, 2)
        pygame.draw.rect(tela, PRETO, botao_sair, 2)

        texto_jogar = fonte_botao.render("Jogar", True, PRETO)
        texto_sair = fonte_botao.render("Sair", True, PRETO)

        tela.blit(texto_jogar, texto_jogar.get_rect(center=botao_jogar.center))
        tela.blit(texto_sair, texto_sair.get_rect(center=botao_sair.center))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    return  # sai do menu e começa o jogo

                if botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    exit()
