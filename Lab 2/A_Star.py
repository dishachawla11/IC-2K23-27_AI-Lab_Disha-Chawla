def a_star(graph, heuristic, start, goal):
    open_list = [start]
    g = {start: 0}

    while open_list:
        current = min(open_list,
                      key=lambda node: g[node] + heuristic[node])

        open_list.remove(current)

        if current == goal:
            print("Goal reached:", current)
            return

        for neighbour, cost in graph[current]:
            new_g = g[current] + cost

            if neighbour not in g or new_g < g[neighbour]:
                g[neighbour] = new_g
                open_list.append(neighbour)

        print(current, end=" -> ")


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# A* Search
a_star(graph, heuristic, 'A', 'F')
