import networkx as nx 
import matplotlib.pyplot as plt

filepath = "./map_text.txt"
with open(filepath) as file:
    data = file.read()
edges = []
for line in data.split("\n"):
    nodes=line.split(" ")
    edge=(int(nodes[0]),int(nodes[1]))
    edges.append(edge)
G = nx.Graph(edges)

layout = nx.spring_layout(G)
plt.figure(1)
nx.draw(G, pos = layout, node_size=5, node_color="green", alpha = 0.5)
plt.title("Base Graph")

load_centrality = nx.load_centrality(G)
dict_load_items=load_centrality.items()
dict_load_items_sorted = sorted(dict_load_items, key=lambda entity:entity[1], reverse = True)
centrality_sorted={k:v for k,v in dict_load_items_sorted}
load_node_ranks=list(centrality_sorted)[:6]
plt.figure(2)
nx.draw(G, pos = layout, node_size=3, node_color="green", alpha = 0.5)
nx.draw(G, pos = layout, node_size=10, node_color="red", nodelist = load_node_ranks, alpha = 1)
plt.title("Highest ranking nodes in Node Centrality")

centrality = nx.degree_centrality(G)
dict_items=centrality.items()
dict_items_sorted = sorted(dict_items, key=lambda entity:entity[1], reverse = True)
centrality_sorted={k:v for k,v in dict_items_sorted}
node_ranks=list(centrality_sorted)[:6]
plt.figure(3)
nx.draw(G, pos = layout, node_size=3, node_color="green", alpha = 0.5)
nx.draw(G, pos = layout, node_size=10, node_color="orange", nodelist = node_ranks, alpha = 1)
plt.title("Highest ranking nodes in Degree Centrality")

plt.show()