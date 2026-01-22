class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(9)] for _ in range(9)]
        self.sub_wins = [[None for _ in range(3)] for _ in range(3)]

    def marcar(self, linha, coluna, jogador):
        if self.grid[linha][coluna] == " ":
            self.grid[linha][coluna] = jogador
            return True
        return False

    def obter(self, linha, coluna):
        return self.grid[linha][coluna]

    def subtabuleiro(self, linha, coluna):
        return linha // 3, coluna // 3


