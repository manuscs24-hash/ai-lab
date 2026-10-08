import heapq

def print_puzzle(s):
    for i in range(0, 9, 3):
        print(*s[i:i+3])
    print()

def manhattan(s, goal):
    distance = 0

    for tile in range(1, 9):
        a = s.index(tile)
        b = goal.index(tile)

        r1, c1 = a // 3, a % 3
        r2, c2 = b // 3, b % 3

        distance += abs(r1 - r2) + abs(c1 - c2)

    return distance

def astar(initial, goal):
    h = manhattan(initial, goal)
    pq = [(h, 0, initial, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))
        h = manhattan(state, goal)

        path = path + [(state, g, h, f)]

        if state == goal:
            return path

        zero = state.index(0)
        r, c = zero // 3, zero % 3

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new = state.copy()
                nz = nr * 3 + nc

                new[zero], new[nz] = new[nz], new[zero]

                if tuple(new) not in visited:
                    ng = g + 1
                    nh = manhattan(new, goal)

                    heapq.heappush(
                        pq,
                        (ng + nh, ng, new, path)
                    )

    return None


initial = [1, 2, 3,
           4, 0, 6,
           7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

print("========================================")
print("       A* - MANHATTAN DISTANCE")
print("========================================")

print("\nInitial State:")
print_puzzle(initial)

print("Goal State:")
print_puzzle(goal)

solution = astar(initial, goal)

if solution:
    for i, (state, g, h, f) in enumerate(solution):
        print("Step", i)
        print_puzzle(state)
        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) =", f)

    print("GOAL FOUND!")
    print("Total Cost =", len(solution) - 1)

else:
    print("No solution")