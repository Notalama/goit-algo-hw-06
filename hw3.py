import networkx as nx
import matplotlib.pyplot as plt

# Визначення районів міста Львова (вузлів)
rayony = ['Zaliznychnyy', 'Lychakivskyy', 'Sykhivskyy',
          'Frankivskyy', 'Shevchenkivskyy', 'Halytskyy']

# Визначення маршрутів (ребер) з вагами (час поїздки в хвилинах)
marshruti = [('Zaliznychnyy', 'Lychakivskyy', {'weight': 20}),
            ('Zaliznychnyy', 'Shevchenkivskyy', {'weight': 15}),
            ('Zaliznychnyy', 'Frankivskyy', {'weight': 25}),
            ('Lychakivskyy', 'Shevchenkivskyy', {'weight': 10}),
            ('Lychakivskyy', 'Sykhivskyy', {'weight': 30}),
            ('Sykhivskyy', 'Frankivskyy', {'weight': 35}),
            ('Halytskyy', 'Zaliznychnyy', {'weight': 10}),
            ('Halytskyy', 'Lychakivskyy', {'weight': 15}),
            ('Halytskyy', 'Shevchenkivskyy', {'weight': 5})]

# Створення графа
graph_mista = nx.Graph()
graph_mista.add_nodes_from(rayony)
graph_mista.add_edges_from(marshruti)

# Алгоритм Дейкстри
def dijkstra(graph, start_node):
    shortest_paths = {node: float('inf') for node in graph.nodes()}
    shortest_paths[start_node] = 0
    visited = set()

    while len(visited) != len(graph.nodes()):
        min_distance = float('inf')
        current_node = None
        for node in graph.nodes():
            if node not in visited and shortest_paths[node] < min_distance:
                min_distance = shortest_paths[node]
                current_node = node

        if current_node is None:
            break

        visited.add(current_node)
        for neighbor in graph[current_node]:
            new_distance = shortest_paths[current_node] + graph[current_node][neighbor]['weight']
            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance

    return shortest_paths

# Знаходження найкоротших шляхів між усіма парами вершин
for start_node in graph_mista.nodes():
    shortest_paths = dijkstra(graph_mista, start_node)
    for end_node in shortest_paths:
        if start_node != end_node:
            path = nx.shortest_path(graph_mista, source=start_node, target=end_node, weight='weight')
            path_length = shortest_paths[end_node]
            print(f"Найкоротший шлях від {start_node} до {end_node}: {path}, довжина: {path_length}")

# Візуалізація графа (залишаємо без змін)
nx.draw(graph_mista, with_labels=True, node_color='skyblue', node_size=1500, font_size=10)
plt.show()