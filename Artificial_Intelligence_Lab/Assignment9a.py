def minimax(node, depth, player)

if depth == 0
return value(node)

if player == 'MAX'
alpha = -inf
for every child of node
value = minimax (child,depth-1,'MIN’)
alpha = max(alpha, value)
return (alpha)

else

set alpha = +inf
for every child of node
value = minimax (child,depth-1,'MAX’)
alpha = min(alpha, value)
return (alpha)

