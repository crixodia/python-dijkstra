import dijkstra
import draw_graph as dg

print(dijkstra.find_all(dijkstra.wmat, 0))
dg.undirected_graph(dijkstra.wmat,"dijkstra_example")