import itertools

def tsp(distance):
    n = len(distance)
    cities = list(range(n))
    
    min_path = None
    min_cost = float('inf')
    
    # Fix starting city as 0
    for perm in itertools.permutations(cities[1:]):
        path = (0,) + perm + (0,)
        
        cost = 0
        for i in range(len(path) - 1):
            cost += distance[path[i]][path[i+1]]
        
        if cost < min_cost:
            min_cost = cost
            min_path = path
            
    return min_path, min_cost


# ---- User Input ----
n = int(input("Enter number of cities: "))
print("Enter distance matrix:")

distance = []
for i in range(n):
    row = list(map(int, input().split()))
    distance.append(row)

path, cost = tsp(distance)

# ---- Output ----
print("\nShortest Path:", path)
print("Minimum Cost:", cost)
