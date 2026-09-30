def hill_climbing(values, start):
    current = start

    while True:
        neighbour = current + 1

        if neighbour >= len(values):
            break

        if values[neighbour] > values[current]:
            current = neighbour
        else:
            break

    return current, values[current]


# Values of different states
values = [2, 5, 8, 12, 10, 7]

# Start from state 0
state, value = hill_climbing(values, 0)

print("Best state:", state)
print("Best value:", value)
