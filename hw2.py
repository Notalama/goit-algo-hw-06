# Алгоритм DFS
def dfs(graph, start_node, end_node):
    visited = set()
    stack = [(start_node, [start_node])]
    while stack:
        (node, path) = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == end_node:
                return path
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))
    return None

# Алгоритм BFS
def bfs(graph, start_node, end_node):
    visited = set()
    queue = [(start_node, [start_node])]
    while queue:
        (node, path) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end_node:
                return path
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return None

def testData(graph_mista):
    start_node = 'Zaliznychnyy'
    end_node = 'Sykhivskyy'
    dfs_path = dfs(graph_mista, start_node, end_node)
    bfs_path = bfs(graph_mista, start_node, end_node)
    print("Шлях DFS:", dfs_path)
    print("Шлях BFS:", bfs_path)
