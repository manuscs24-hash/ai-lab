def print_puzzle(p):
    print()
    for i in range(0, 9, 3):
        print(p[i:i+3])
    print()
puzzle = [1, 2, 3,
          4, 0, 5,
          7, 8, 6]
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]
print("8 PUZZLE")
print("W = Up | S = Down | A = Left | D = Right")
while puzzle != goal:
    print_puzzle(puzzle)
    move = input("Move: ").lower()
    zero = puzzle.index(0)
    row = zero // 3
    col = zero % 3
    if move == "w":
        new_row, new_col = row - 1, col
    elif move == "s":
        new_row, new_col = row + 1, col
    elif move == "a":
        new_row, new_col = row, col - 1
    elif move == "d":
        new_row, new_col = row, col + 1
    else:
        print("Use W, A, S or D")
        continue
    if 0 <= new_row < 3 and 0 <= new_col < 3:
        new_zero = new_row * 3 + new_col
        puzzle[zero], puzzle[new_zero] = \
            puzzle[new_zero], puzzle[zero]
    else:
        print("Invalid move")
print_puzzle(puzzle)
print("GOAL REACHED!")