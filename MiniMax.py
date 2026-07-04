class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children else []

def minimax(node, depth, maximizing_player):
    # Base case: leaf node -> return its value
    if not node.children:
        return node.value

    if maximizing_player:
        best = -1000000
        for child in node.children:
            val = minimax(child, depth + 1, False)
            best = max(best, val)
        return best
    else:
        best = 1000000
        for child in node.children:
            val = minimax(child, depth + 1, True)
            best = min(best, val)
        return best


# Same tree as before
leaf_a = Node(3)
leaf_b = Node(5)
leaf_c = Node(6)
leaf_d = Node(9)

min_node1 = Node(children=[leaf_a, leaf_b])
min_node2 = Node(children=[leaf_c, leaf_d])

root = Node(children=[min_node1, min_node2])

result = minimax(root, 0, True)
print("Optimal value:", result)