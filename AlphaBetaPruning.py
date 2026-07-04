class Node:
    def __init__(self, value=None, children=None):
        self.value = value        
        self.children = children if children else [] 

def alphabeta(node, depth, alpha, beta, maximizing_player):
    
    if not node.children:
        return node.value

    if maximizing_player:
        best = -1000000   
        for child in node.children:
            val = alphabeta(child, depth + 1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if alpha >= beta:
                print(f"   Pruned remaining children at depth {depth} (MAX node)")
                break 
        return best
    else:
        best = 1000000   
        for child in node.children:
            val = alphabeta(child, depth + 1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if alpha >= beta:
                print(f"   Pruned remaining children at depth {depth} (MIN node)")
                break   
        return best

leaf_a = Node(3)
leaf_b = Node(5)
leaf_c = Node(6)
leaf_d = Node(9)

min_node1 = Node(children=[leaf_a, leaf_b])
min_node2 = Node(children=[leaf_c, leaf_d])

root = Node(children=[min_node1, min_node2]) 

result = alphabeta(root, 0, -1000000, 1000000, True)
print("Optimal value:", result)