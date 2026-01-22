class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(9)] for _ in range(9)]

    def obter(self, l, c):
        return self.grid[l][c]

    def definir(self, l, c, v):
        if self.grid[l][c] == " ":
            self.grid[l][c] = v
            return True
        return False

    def verificar_vitoria(self):
        for bl in range(0, 9, 3):
            for bc in range(0, 9, 3):
                vencedor = self._verificar_bloco(bl, bc)
                if vencedor:
                    return vencedor, (bl, bc)
        return None, None

    def _verificar_bloco(self, bl, bc):
        g = self.grid
        for i in range(3):
            if g[bl+i][bc] == g[bl+i][bc+1] == g[bl+i][bc+2] != " ":
                return g[bl+i][bc]
            if g[bl][bc+i] == g[bl+1][bc+i] == g[bl+2][bc+i] != " ":
                return g[bl][bc+i]

        if g[bl][bc] == g[bl+1][bc+1] == g[bl+2][bc+2] != " ":
            return g[bl][bc]
        if g[bl][bc+2] == g[bl+1][bc+1] == g[bl+2][bc] != " ":
            return g[bl][bc+2]

        return None
           
    def cheio(self):
     for linha in self.grid:
        if " " in linha:
            return False
     return True




