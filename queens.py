N = 8

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve(col, board):
    if col == N:
        print("Solution:", board)
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i

            if solve(col + 1, board):
                return True

            board[col] = -1   # backtracking

    return False

board = [-1] * N
solve(0, board)
