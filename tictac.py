board = [" "]*9

def print_board():
    for i in range(0,9,3):
        print(board[i], "|", board[i+1], "|", board[i+2])

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]==board[b]==board[c] and board[a]!=" ":
            return board[a]
    return None

player = "X"
for i in range(9):
    print_board()
    move = int(input("Enter position (0-8): "))
    board[move] = player

    winner = check_winner()
    if winner:
        print_board()
        print("Winner:", winner)
        break

    player = "O" if player=="X" else "X"
else:
    print("Draw")
