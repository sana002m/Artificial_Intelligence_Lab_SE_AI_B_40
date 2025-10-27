def minimax(node, depth, maximizingPlayer, values, index=0):
    # Leaf node condition
    if depth == 0 or index >= len(values):
        return values[index]

    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):  # Two children for each node
            val = minimax(node*2+i, depth-1, False, values, index*2+i)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(node*2+i, depth-1, True, values, index*2+i)
            best = min(best, val)
        return best


# Example: Game tree with depth = 3
values = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
depth = 3
result = minimax(0, depth, True, values)

print("Optimal value (using Minimax):", result)

