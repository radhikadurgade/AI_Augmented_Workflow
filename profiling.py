
from collections import deque
from time import perf_counter

# Same graph for both algorithms
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

START = "A"
GOAL = "G"
RUNS = 100


def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    return nodes_expanded


def dfs(start, goal):
    stack = [start]
    visited = {start}
    nodes_expanded = 0

    while stack:
        node = stack.pop()
        nodes_expanded += 1

        if node == goal:
            break

        # Reverse order for consistent traversal
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return nodes_expanded


def profile(name, algorithm):
    total_time = 0
    nodes = 0

    for _ in range(RUNS):
        start_time = perf_counter()
        nodes = algorithm(START, GOAL)
        end_time = perf_counter()

        total_time += end_time - start_time

    avg_ms = (total_time / RUNS) * 1000

    print(f"\n{name}")
    print(f"Average time: {avg_ms:.6f} ms")
    print(f"Nodes expanded: {nodes}")


print("SLE-2: BFS vs DFS Profiling")
print("Start:", START, "| Goal:", GOAL)
print("Runs:", RUNS)

profile("BFS", bfs)
profile("DFS", dfs)