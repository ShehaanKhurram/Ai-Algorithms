import heapq
h = {
    'S': 32,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0,
}

graph = {
    'S': [('B', 4), ('C', 3)],
    'B': [('E', 12), ('F', 5)],
    'C': [('E', 10), ('D', 7)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)],
    'G': []
}

def Astar(graph, h, root, goal):
    visited = set()
    pq = [(h[root], 0, root)]

    while pq:
        f, cost, node = heapq.heappop(pq)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == goal:
                print("\nGoal found at cost:", cost)
                return
            
            for i, w in graph[node]:
                new_cost = cost + w
                new_f = new_cost + h[i]
                heapq.heappush(pq, (new_f, new_cost, i))




root = 'S'
goal = 'G'

Astar(graph, h, root, goal)
