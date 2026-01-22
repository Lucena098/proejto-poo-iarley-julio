from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.jogador_atual = "X"
        self.pontos = {"X": 0, "O": 0}

    def alternar_jogador(self):
        self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def jogar(self, linha, coluna):
        if self.board.marcar(linha, coluna, self.jogador_atual):
            # Aqui depois entra a lógica de vitória do 3x3
            self.alternar_jogador()
