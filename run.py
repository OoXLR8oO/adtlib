from adtlib.algorithms.traversal import bfs, dfs
from adtlib.graph import Graph
from adtlib.node import GraphNode

# Create graph
graph = Graph[str](_directed=False)

# Create nodes
nodes = {name: GraphNode(name) for name in "ABCDEFGHIJ"}

# Add nodes to graph
for node in nodes.values():
    graph.add_node(node)

# Add edges
graph.add_edge(nodes["A"], nodes["B"])
graph.add_edge(nodes["A"], nodes["C"])

graph.add_edge(nodes["B"], nodes["D"])
graph.add_edge(nodes["B"], nodes["E"])

graph.add_edge(nodes["D"], nodes["H"])
graph.add_edge(nodes["E"], nodes["H"])

graph.add_edge(nodes["F"], nodes["I"])
graph.add_edge(nodes["G"], nodes["I"])

graph.add_edge(nodes["I"], nodes["J"])

# # Run traversals
print("BFS from A:", bfs(graph, graph.get_node("A")))
print("DFS from A:", dfs(graph, graph.get_node("A")))