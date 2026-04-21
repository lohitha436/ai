from collections import deque

def water_jug(a, b, target):
    visited = set()
    queue = deque([(0,0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        print(x, y)
        visited.add((x, y))

        if x == target or y == target:
            print("Target reached")
            return

        queue.append((a, y))   # fill A
        queue.append((x, b))   # fill B
        queue.append((0, y))   # empty A
        queue.append((x, 0))   # empty B
        queue.append((min(a, x+y), max(0, x+y-a)))  # pour A→B
        queue.append((max(0, x+y-b), min(b, x+y)))  # pour B→A

    print("No solution")
