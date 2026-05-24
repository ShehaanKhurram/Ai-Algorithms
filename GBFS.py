import heapq
h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 6,
    'F': 1,
    'G': 0,   # goal
    'H': 3,
    'I': 4,
    'J': 0
}

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['H', 'I'],
    'D': ['F', 'G'],
    'E': [],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

def GBFS(graph, h, root, goal):
    visited = set()
    pq = [(h[root],root)]

    while pq:
        heu, node = heapq.heappop(pq)

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == goal:
                print("\nGoal found:",node)
                return

            for i in graph[node]:
                heapq.heappush(pq, (h[i], i))

root = 'A'
goal = 'G'

GBFS(graph, h, root, goal)