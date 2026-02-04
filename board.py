
class Cell:
    def __init__(self):
        self.value = None


class SmallBoard:
    def __init__(self):
        self.cells = [[Cell() for _ in range(3)] for _ in range(3)]
        self.winner = None  # X, O, E (empate)

    def is_full(self):
        return all(self.cells[r][c].value for r in range(3) for c in range(3))

    def check_winner(self):
        lines = []

        lines.extend(self.cells)
        lines.extend([[self.cells[r][c] for r in range(3)] for c in range(3)])
        lines.append([self.cells[i][i] for i in range(3)])
        lines.append([self.cells[i][2 - i] for i in range(3)])

        for line in lines:
            if line[0].value and all(cell.value == line[0].value for cell in line):
                self.winner = line[0].value
                return

        if self.is_full():
            self.winner = "E"


class BigBoard:
    def __init__(self):
        self.boards = [[SmallBoard() for _ in range(3)] for _ in range(3)]
        self.winner = None

    def check_winner(self):
        grid = [[b.winner for b in row] for row in self.boards]

        for i in range(3):
            if grid[i][0] and grid[i][0] != "E" and all(grid[i][j] == grid[i][0] for j in range(3)):
                self.winner = grid[i][0]
                return
            if grid[0][i] and grid[0][i] != "E" and all(grid[j][i] == grid[0][i] for j in range(3)):
                self.winner = grid[0][i]
                return

        if grid[0][0] and grid[0][0] != "E" and all(grid[i][i] == grid[0][0] for i in range(3)):
            self.winner = grid[0][0]
            return
        if grid[0][2] and grid[0][2] != "E" and all(grid[i][2 - i] == grid[0][2] for i in range(3)):
            self.winner = grid[0][2]
            return

        
        # ✅ EMPATE GLOBAL
        if all(b.winner for row in self.boards for b in row):
            self.winner = "E"
