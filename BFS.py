#from collections import deque
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

def BFS(graph, root):
    visited = set()

    #q = deque([root])
    q = [root]

    while q:
        #node = q.popleft()
        node = q.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for i in graph[node]:
                q.append(i)

print("BFS:", end=" ")
BFS(graph, 'A')
