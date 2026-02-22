from adtlib.node import GraphNode, LinkedNode, TreeNode
from adtlib.stack import Stack
from adtlib.queue import Queue
from adtlib.graph import Graph

# n1 = GraphNode(1)
# n2 = GraphNode(2)

# ln1 = LinkedNode(4)
# ln2 = LinkedNode(5)

# n1.add_neighbour(n2)
# n2.add_neighbour(n1)

# n1.remove_neighbour(n2)

# ln1.add_next(ln2)

# print(n1)
# print(n2)

# print(ln1)
# print(ln2)

# s1 = Stack()
# s1.push(1)
# s1.push(2)
# s1.push('3')

# print(s1)
# print(s1.pop())
# print(s1)

# q1 = Queue()
# q1.enqueue(n1)
# q1.enqueue(n2)
# q1.enqueue(5)
# print(q1)

# q1.dequeue()
# print(q1)

# graph = Graph(_directed=False)

# for value in ["A", "B", "C", "D", "E", "F", "G", "H"]:
#     graph.add_node(GraphNode(value))

# a = graph.get_node("A")
# b = graph.get_node("B")
# c = graph.get_node("C")
# d = graph.get_node("D")
# e = graph.get_node("E")
# f = graph.get_node("F")
# g = graph.get_node("G")
# h = graph.get_node("H")

# graph.add_edge(a, b)
# graph.add_edge(a, c)
# graph.add_edge(b, d)
# graph.add_edge(c, d)
# graph.add_edge(d, e)
# graph.add_edge(e, f)
# graph.add_edge(f, g)
# graph.add_edge(g, h)
# graph.add_edge(h, a)

# for node in graph.nodes:
#     print(f"{node.value}: {[n.value for n in node.neighbours]}")

# print("BFS traversal starting at A:", graph.bfs(a))
# print("DFS traversal starting at A:", graph.dfs(a))

# graph.remove_edge(a, c)

# print("\nAfter removing edge A-C:")
# for node in graph.nodes:
#     print(f"{node.value}: {[n.value for n in node.neighbours]}")

# print("BFS traversal starting at A:", graph.bfs(a))
# print("DFS traversal starting at A:", graph.dfs(a))


# print("===================================================================")


# # =========================
# # Directed Graph
# # =========================

# graph = Graph(_directed=True)

# for value in ["A", "B", "C", "D", "E", "F", "G", "H"]:
#     graph.add_node(GraphNode(value))

# a = graph.get_node("A")
# b = graph.get_node("B")
# c = graph.get_node("C")
# d = graph.get_node("D")
# e = graph.get_node("E")
# f = graph.get_node("F")
# g = graph.get_node("G")
# h = graph.get_node("H")

# graph.add_edge(a, b)
# graph.add_edge(a, c)
# graph.add_edge(b, d)
# graph.add_edge(c, d)
# graph.add_edge(d, e)
# graph.add_edge(e, f)
# graph.add_edge(f, g)
# graph.add_edge(g, h)
# graph.add_edge(h, a)

# for node in graph.nodes:
#     print(f"{node.value}: {[n.value for n in node.neighbours]}")

# print("Directed BFS starting at A:", graph.bfs(a))
# print("Directed DFS starting at A:", graph.dfs(a))
# print("")
# print(graph.get_node("A").children)
# print(graph.get_node("A").neighbours)

# Create nodes
root = TreeNode("root")
left_child = TreeNode("left")
right_child = TreeNode("right")
right_right_child = TreeNode("right right")

# Link children to root
root.left = left_child
root.right = right_child
right_child.right = right_right_child

# Access neighbours (children)
print(root.neighbours)  # [left_child, right_child]

# Iterate over neighbours
for child in root.neighbours:
    print(f"Child value: {child.value}")

# Output:
# [TreeNode(value=left, left=None, right=None), TreeNode(value=right, left=None, right=right right)]
# Child value: left
# Child value: right