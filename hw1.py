import networkx as nx
import matplotlib.pyplot as plt
from hw2 import testData

nodes = ['Zaliznychnyy', 'Lychakivskyy', 'Sykhivskyy', 'Frankivskyy', 'Shevchenkivskyy', 'Halytskyy']

edges = [('Zaliznychnyy', 'Lychakivskyy'), ('Zaliznychnyy', 'Shevchenkivskyy'),
            ('Zaliznychnyy', 'Frankivskyy'), ('Lychakivskyy', 'Shevchenkivskyy'),
            ('Lychakivskyy', 'Sykhivskyy'), ('Sykhivskyy', 'Frankivskyy'),
            ('Halytskyy', 'Zaliznychnyy'), ('Halytskyy', 'Lychakivskyy'), ('Halytskyy', 'Shevchenkivskyy')]

graph_mista = nx.Graph()
graph_mista.add_nodes_from(nodes)
graph_mista.add_edges_from(edges)

nx.draw(graph_mista, with_labels=True, node_color='skyblue', node_size=1500, font_size=10)
plt.show()

print("Кількість вершин:", graph_mista.number_of_nodes())
print("Кількість ребер:", graph_mista.number_of_edges())
print("Ступені вершин:", dict(graph_mista.degree()))


# Завдання 2
testData(graph_mista)