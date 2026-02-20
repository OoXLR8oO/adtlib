from adtlib.node import GraphNode, LinkedNode
from adtlib.stack import Stack
from adtlib.queue import Queue

n1 = GraphNode(1)
n2 = GraphNode(2)

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

q1 = Queue()
q1.enqueue(n1)
q1.enqueue(n2)
q1.enqueue(5)
print(q1)

q1.dequeue()
print(q1)