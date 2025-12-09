from config import BOARD_SIZE

def check_new_triples(board, player, scored_positions):
    new_points = 0
    new_scored = []

    # Horizontal
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE - 2):
            if board[row][col] == board[row][col+1] == board[row][col+2] == player:
                triple = (row, col, "H")
                if triple not in scored_positions:
                    new_points += 1
                    new_scored.append(triple)

    # Vertical
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE - 2):
            if board[row][col] == board[row+1][col] == board[row+2][col] == player:
                triple = (row, col, "V")
                if triple not in scored_positions:
                    new_points += 1
                    new_scored.append(triple)

    # Diagonal 1
    for row in range(BOARD_SIZE - 2):
        for col in range(BOARD_SIZE - 2):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == player:
                triple = (row, col, "D1")
                if triple not in scored_positions:
                    new_points += 1
                    new_scored.append(triple)

    # Diagonal 2
    for row in range(BOARD_SIZE - 2):
        for col in range(2, BOARD_SIZE):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == player:
                triple = (row, col, "D2")
                if triple not in scored_positions:
                    new_points += 1
                    new_scored.append(triple)

    return new_points, new_scored

def is_board_full(board):
    return all(cell != "" for row in board for cell in row)


