import math

def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    
    # leaf node
    if depth == 0:
        return values[node_index]
    
    if maximizing_player:
        best = -math.inf
        
        for i in range(2):
            val = alpha_beta(depth-1, node_index*2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            if beta <= alpha:
                break   # beta cut-off
        
        return best
    
    else:
        best = math.inf
        
        for i in range(2):
            val = alpha_beta(depth-1, node_index*2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            if beta <= alpha:
                break   # alpha cut-off
        
        return best


# ---- User Input ----
values = list(map(int, input("Enter leaf node values (space separated): ").split()))
depth = int(input("Enter depth of tree: "))

result = alpha_beta(depth, 0, True, values, -math.inf, math.inf)

# ---- Output ----
print("\nOptimal value using Alpha-Beta Pruning:", result)
