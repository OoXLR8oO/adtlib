from adtlib.algorithms.traversal import bfs, dfs
from adtlib.graph import Graph
from adtlib.node import GraphNode

# Create graph
graph = Graph[str](_directed=False)

# Create nodes A-Z
nodes = {name: GraphNode(name) for name in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

# Add nodes to graph
for node in nodes.values():
    graph.add_node(node)

# Main spine
graph.add_edge(graph.get_node("A"), graph.get_node("B"))
graph.add_edge(graph.get_node("B"), graph.get_node("C"))
graph.add_edge(graph.get_node("C"), graph.get_node("D"))
graph.add_edge(graph.get_node("D"), graph.get_node("E"))
graph.add_edge(graph.get_node("E"), graph.get_node("F"))
graph.add_edge(graph.get_node("F"), graph.get_node("G"))
graph.add_edge(graph.get_node("G"), graph.get_node("H"))
graph.add_edge(graph.get_node("H"), graph.get_node("I"))
graph.add_edge(graph.get_node("I"), graph.get_node("J"))

# Branches off spine
graph.add_edge(graph.get_node("C"), graph.get_node("K"))
graph.add_edge(graph.get_node("K"), graph.get_node("L"))
graph.add_edge(graph.get_node("L"), graph.get_node("M"))

graph.add_edge(graph.get_node("E"), graph.get_node("N"))
graph.add_edge(graph.get_node("N"), graph.get_node("O"))
graph.add_edge(graph.get_node("O"), graph.get_node("P"))

graph.add_edge(graph.get_node("G"), graph.get_node("Q"))
graph.add_edge(graph.get_node("Q"), graph.get_node("R"))

# Cross connections creating cycles
graph.add_edge(graph.get_node("L"), graph.get_node("F"))
graph.add_edge(graph.get_node("O"), graph.get_node("H"))
graph.add_edge(graph.get_node("R"), graph.get_node("D"))

# Dead end chain
graph.add_edge(graph.get_node("J"), graph.get_node("S"))
graph.add_edge(graph.get_node("S"), graph.get_node("T"))
graph.add_edge(graph.get_node("T"), graph.get_node("U"))

# Separate disconnected component
graph.add_edge(graph.get_node("V"), graph.get_node("W"))
graph.add_edge(graph.get_node("W"), graph.get_node("X"))
graph.add_edge(graph.get_node("X"), graph.get_node("Y"))
graph.add_edge(graph.get_node("Y"), graph.get_node("Z"))
graph.add_edge(graph.get_node("Z"), graph.get_node("V"))

# Run traversals
print("BFS from A:", bfs(graph, graph.get_node("A")))
print("DFS from A:", dfs(graph, graph.get_node("A")))