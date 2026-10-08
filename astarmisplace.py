import heapq

def print_puzzle(s):
    for i in range(0, 9, 3):
        print(*s[i:i+3])
    print()

def misplaced(s, goal):
    return sum(s[i] != goal[i] and s[i] != 0 for i in range(9))

def astar(initial, goal):
    h = misplaced(initial, goal)
    pq = [(h, 0, initial, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))
        h = misplaced(state, goal)

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
                    nh = misplaced(new, goal)

                    heapq.heappush(
                        pq,
                        (ng + nh, ng, new, path)
                    )

    return None


initial = [2, 8, 3,
           1, 0, 4,
           7, 6, 5]

goal = [1, 2, 3,
        8, 0, 4,
        7, 6, 5]

print("========================================")
print("       A* - MISPLACED TILES")
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