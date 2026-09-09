from collections import deque

def water_jug(jug1, jug2, target):

    queue = deque()
    visited = set()

    queue.append((0, 0))
    visited.add((0, 0))

    while queue:

        a, b = queue.popleft()

        print("Current State:", (a, b))

        if a == target or b == target:
            print("Target reached!")
            return

        states = [
            (jug1, b),              # Fill Jug 1
            (a, jug2),              # Fill Jug 2
            (0, b),                 # Empty Jug 1
            (a, 0),                 # Empty Jug 2
            (a - min(a, jug2-b), b + min(a, jug2-b)),  # Pour Jug 1 -> Jug 2
            (a + min(b, jug1-a), b - min(b, jug1-a))   # Pour Jug 2 -> Jug 1
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("Target cannot be reached.")


# Jug capacities
jug1 = 4
jug2 = 3

# Target amount
target = 2

water_jug(jug1, jug2, target)
