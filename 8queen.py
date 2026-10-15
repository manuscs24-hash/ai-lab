
import random
import math

N = 8
def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def simulated_annealing():
    board = [random.randint(0, N - 1) for _ in range(N)]

    temperature = 100.0
    cooling_rate = 0.99
    min_temperature = 0.01
    max_iterations = 100000

    for iteration in range(max_iterations):
        current_cost = heuristic(board)

        if current_cost == 0:
            return board, iteration

        new_board = board.copy()
        col = random.randint(0, N - 1)
        new_row = random.randint(0, N - 1)

        while new_row == new_board[col]:
            new_row = random.randint(0, N - 1)

        new_board[col] = new_row
        new_cost = heuristic(new_board)

        delta = new_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            board = new_board

        temperature *= cooling_rate

        if temperature < min_temperature:
            temperature = 100.0

    return None, max_iterations

solution, iterations = simulated_annealing()

if solution is not None:
    print("Solution found!")
    print("Board:", solution)
    print("Iterations:", iterations)

    for row in range(N):
        print(" ".join(
            "Q" if solution[col] == row else "."
            for col in range(N)
        ))
else:
    print("Solution not found. Try running again.")
