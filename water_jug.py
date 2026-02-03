from collections import deque

def water_jug(cap1, cap2, target):
    q = deque()
    q.append((0, 0, [(0, 0)]))   
    visited = set()
    visited.add((0, 0))

    while q:
        x, y, path = q.popleft()

        if x == target or y == target:
            print("Solution path:")
            for p in path:
                print(p)
            return

        
        states = [
            (cap1, y),    # fill jug1
            (x, cap2),    # fill jug2
            (0, y),       # empty jug1
            (x, 0),       # empty jug2
            (x + min(y, cap1 - x), y - min(y, cap1 - x)),  # pour jug2 -> jug1
            (x - min(x, cap2 - y), y + min(x, cap2 - y))   # pour jug1 -> jug2
        ]

        for nx, ny in states:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, path + [(nx, ny)]))

    print("No solution")



a = int(input("Enter capacity of jug 1: "))
b = int(input("Enter capacity of jug 2: "))
t = int(input("Enter target: "))

water_jug(a, b, t)
