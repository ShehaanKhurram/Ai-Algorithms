graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['H', 'I'],
    'D' : ['F', 'G'],
    'E' : [],
    'F' : ['J'],
    'G' : [],
    'H' : [],
    'I' : [],
    'J' : [],
    'K' : []
}

def DLS(graph, root, limit):
    visited = set()
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if depth < limit:
                for i in reversed(graph[node]):
                    stack.append((i, depth+1)) 


def IDDFS(graph, root, max_Limit):
    for limit in range(max_Limit + 1):
        print("\nDepth ", limit, ": ", end = " ")
        DLS(graph, root, limit)

max_Limit = 3
root = 'A'
IDDFS(graph, root, max_Limit)