# graph = {
#     'A' : ['B', 'C'],
#     'B' : ['D', 'E'],
#     'C' : ['H', 'I'],
#     'D' : ['F', 'G'],
#     'E' : [],
#     'F' : ['J'],
#     'G' : [],
#     'H' : [],
#     'I' : [],
#     'J' : [],
#     'K' : []
# }

graph = {
    '1' : ['2', '4', '5'],
    '2' : ['3'],
    '3' : [],
    '4' : ['6', '7'],
    '5' : ['8'],
    '6' : ['9'],
    '7' : [],
    '8' : [],
    '9' : []
}

def DFS(grapgh, root):
    visited = set()
    stack = [root]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for i in graph[node]:
                stack.append(i)


print("DFS:", end=" ")
DFS(graph, '1')