def best_first_search(graph, heuristic, start, goal):
    open_list = [start]
    visited = set()

    while open_list:
        # Choose the node with the lowest heuristic value
        current = min(open_list, key=lambda node: heuristic[node])
        open_list.remove(current)

        print(current, end=" ")

        if current == goal:
            print("\nGoal found!")
            return

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in open_list:
                open_list.append(neighbour)

    print("\nGoal not found!")


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# Start Best First Search
best_first_search(graph, heuristic, 'A', 'F')
