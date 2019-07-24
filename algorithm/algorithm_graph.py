# undirected graph
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']
         }


def bfs(graph, start):
    """
    - queue
    """
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            # queue.extend(graph[vertex] - set(visited))
            queue.extend(graph[vertex])
    return visited


def bfs_paths(graph, start, goal):
    """
    - return the shortest path for the first
    """
    queue = [(start, [start])]
    visited = []

    while queue:
        vertex, path = queue.pop(0)
        if vertex == goal:
            visited.append(path)
        else:
            for next_vertex in set(graph[vertex]) - set(path):
                queue.append((next_vertex, path + [next_vertex]))
    return visited


def dfs(graph, start):
    """
    - stack
    """
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            # stack.extend(graph[vertex] - set(visited))
            stack.extend(graph[vertex])
    return visited


def dfs_paths(graph, start, goal):
    """
    """
    stack = [(start, [start])]
    visited = []

    while stack:
        vertex, path = stack.pop()
        if vertex == goal:
            visited.append(path)
        else:
            for next_vertex in set(graph[vertex]) - set(path):
                stack.append((next_vertex, path + [next_vertex]))
    return visited


if __name__ == "__main__":
    visited = bfs(graph, 'A')
    print(visited)

    visited = bfs_paths(graph, 'A', 'F')
    print(visited)

    visited = dfs(graph, 'A')
    print(visited)

    visited = dfs_paths(graph, 'A', 'F')
    print(visited)

