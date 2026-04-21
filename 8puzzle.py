from collections import deque

start = "123456780"
goal = "123456708"

moves = [(0,1),(1,2),(3,4),(4,5),(6,7),(7,8),
         (0,3),(3,6),(1,4),(4,7),(2,5),(5,8)]

def solve(start):
    queue = deque([(start, "")])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        visited.add(state)
        zero = state.index('0')

        for i,j in moves:
            if zero == i:
                new = list(state)
                new[i], new[j] = new[j], new[i]
                new = "".join(new)
                if new not in visited:
                    queue.append((new, path+"->"+new))
    return "No solution"

print(solve(start))
