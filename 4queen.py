import random

N = 8

def cost(state):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing():
    state = [random.randint(0, N - 1) for _ in range(N)]

    while True:
        current_cost = cost(state)
        print("State:", state, "Cost:", current_cost)

        if current_cost == 0:
            print("Goal State Found!")
            return

        neighbors = []

        for col in range(N):
            for row in range(N):
                if row != state[col]:
                    new_state = state.copy()
                    new_state[col] = row
                    neighbors.append(new_state)

        best_state = min(neighbors, key=cost)

        if cost(best_state) < current_cost:
            state = best_state
        else:
            print("Local minimum reached. Restarting...")
            state = [random.randint(0, N - 1) for _ in range(N)]

hill_climbing()
