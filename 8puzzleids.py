def print_puzzle(p):
    for i in range(0, 9, 3):
        print(p[i:i+3])
    print()


def dls(state, goal, depth, path):
    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    r, c = zero // 3, zero % 3

    for dr, dc, move in [(-1,0,"U"), (1,0,"D"),
                         (0,-1,"L"), (0,1,"R")]:

        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new = state.copy()
            new[zero], new[nr*3+nc] = new[nr*3+nc], new[zero]

            if new not in path:
                result = dls(new, goal, depth - 1, path + [new])

                if result:
                    return result

    return None


def IDS(initial, goal):
    for depth in range(20):
        print("Searching at depth:", depth)

        result = dls(initial, goal, depth, [initial])

        if result:
            return result

    return None


initial = [1, 2, 3,
           4, 0, 5,
           7, 8, 6]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

print("INITIAL STATE")
print_puzzle(initial)

print("GOAL STATE")
print_puzzle(goal)

solution = IDS(initial, goal)

if solution:
    print("GOAL FOUND!")
    print("Solution Path:")
    print()

    for i, state in enumerate(solution):
        print("Step", i)
        print_puzzle(state)

    print("Total Moves:", len(solution) - 1)
else:
    print("No Solution")