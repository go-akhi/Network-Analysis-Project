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
#print(G)
layout = nx.spring_layout(G)
#nx.draw(G, pos = layout, node_size=2, node_color="blue")
#plt.show()
#print(nx.average_shortest_path_length(G))
#print(stat.mean([G.degree(n) for n in G.nodes()]))
centrality = nx.load_centrality(G)
dict_items=centrality.items()
dict_items_sorted = sorted(dict_items, key=lambda entity:entity[1], reverse = True)
centrality_sorted={k:v for k,v in dict_items_sorted}
node_ranks=list(centrality_sorted)[:8]
nx.draw(G, pos = layout, node_size=3, node_color="green", alpha = 0.5)
nx.draw(G, pos = layout, node_size=80, node_color="blue", nodelist = node_ranks, alpha = 1)
plt.show()
#centrality = nx.degree_centrality(G)
#dict_items=centrality.items()
#dict_items_sorted = sorted(dict_items, key=lambda entity:entity[1], reverse = True)
#centrality_sorted={k:v for k,v in dict_items_sorted}
#node_ranks=list(centrality_sorted)[:8]
#nx.draw(G, pos = layout, node_size=3, node_color="green", alpha = 0.5)
#nx.draw(G, pos = layout, node_size=80, node_color="blue", nodelist = node_ranks, alpha = 1)
#plt.show()
