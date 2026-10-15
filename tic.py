def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    return True


board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

current_player = "X"

while True:
    display_board(board)

    print("Player", current_player, "turn")

    try:
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))

        if row not in range(1, 4) or col not in range(1, 4):
            print("Invalid position")
            continue

        row = row - 1
        col = col - 1

        if board[row][col] != " ":
            print("Invalid move")
            continue

        board[row][col] = current_player

    except ValueError:
        print("Invalid input. Please enter numbers.")
        continue

    if check_winner(board, current_player):
        display_board(board)
        print("Player", current_player, "wins!")
        break

    if board_full(board):
        display_board(board)
        print("Match Draw")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"