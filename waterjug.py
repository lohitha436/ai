def water_jug(a, b, target):
    visited = set()
    queue = [(0,0)]

    while queue:
        x,y = queue.pop(0)
        if (x,y) in visited:
            continue

        print(x,y)
        visited.add((x,y))

        if x==target or y==target:
            print("Target reached")
            return

        queue.append((a,y))
        queue.append((x,b))
        queue.append((0,y))
        queue.append((x,0))
        queue.append((min(a,x+y), max(0,x+y-a)))
        queue.append((max(0,x+y-b), min(b,x+y)))

water_jug(4,3,2)
