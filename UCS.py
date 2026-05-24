import heapq
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('H', 3), ('I', 6)],
    'D': [('F', 1), ('G', 2)],
    'E': [],
    'F': [('J', 2)],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

def UCS(graph, root, goal):
    visited = set()
    pq = [(0, root)]

    while pq:
        cost, node = heapq.heappop(pq)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == goal:
                print("Goal found with cost: ",cost)

            for i, w in graph[node]:
                heapq.heappush(pq, (cost + w, i))


root = 'A'
goal = 'G'
UCS(graph, root, goal)