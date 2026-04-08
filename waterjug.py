from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))  # (jug1, jug2, path)

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path = path + [(x, y)]

        if x == target or y == target:
            return path
        queue.append((jug1, y, path))  
        queue.append((x, jug2, path))  
        queue.append((0, y, path))     
        queue.append((x, 0, path))     

        pour = min(x, jug2 - y)
        queue.append((x - pour, y + pour, path))

        pour = min(y, jug1 - x)
        queue.append((x + pour, y - pour, path))

    return None


# ---- User Input ----
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target quantity: "))

result = water_jug(jug1, jug2, target)

# ---- Output ----
if result:
    print("\nSteps to reach target:")
    for step in result:
        print(step)
else:
    print("No solution possible")
