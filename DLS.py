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
        node, depth= stack.pop()
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if depth < limit:
                for i in graph[node]:
                    stack.append((i, depth+1))

            

depthLimit = 2
root = 'A'
DLS(graph, root, depthLimit)