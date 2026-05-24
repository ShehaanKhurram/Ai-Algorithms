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

h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 6,
    'F': 1,
    'G': 0,
    'H': 3,
    'I': 4,
    'J': 0
}

def HillClimb(graph, h, root, goal):
    current = root

    while(True):
        print(current)

        if current == goal:
            print("\nGoal Reached.!")
            return
        
        neighbor = graph[current]

        if not neighbor:
            return 
        

        best = None

        for nei in neighbor:
            if best is None or h[nei] < h[best]:
                best = nei
                
        if h[current] <= h[best]:
            print("\nStuck at local optimum.!")
            return
        

        current = best


root = 'A'
goal = 'G'
HillClimb(graph, h, root, goal)
