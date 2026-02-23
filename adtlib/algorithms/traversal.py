from typing import List, Set, TypeVar
from adtlib.graph import Graph
from adtlib.node import GraphNode
from adtlib.queue import Queue
from adtlib.stack import Stack

T = TypeVar("T")

def bfs(graph: Graph[T], start: GraphNode[T]) -> List[GraphNode[T]]:
    """
    Perform breadth-first search within a graph starting from a node.

    :param graph: Graph containing nodes
    :type graph: Graph[T]
    :param start: Node to start traversal from
    :type start: GraphNode[T]
    :return: List of nodes in BFS order
    :rtype: List[GraphNode[T]]
    :raises ValueError: If the start node is not part of the graph
    """
    if start not in graph.nodes:
        raise ValueError("Start node is not part of the graph")

    queue = Queue[GraphNode[T]]()
    queue.enqueue(start)
    visited: Set[GraphNode[T]] = set()
    order: List[GraphNode[T]] = []

    while not queue.is_empty():
        node = queue.dequeue()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nbr in node.neighbours:
            if nbr not in visited:
                queue.enqueue(nbr)

    return order


def dfs(graph: Graph[T], start: GraphNode[T]) -> List[GraphNode[T]]:
    """
    Perform depth-first search within a graph starting from a node.

    :param graph: Graph containing nodes
    :type graph: Graph[T]
    :param start: Node to start traversal from
    :type start: GraphNode[T]
    :return: List of nodes in DFS order
    :rtype: List[GraphNode[T]]
    :raises ValueError: If the start node is not part of the graph
    """
    if start not in graph.nodes:
        raise ValueError("Start node is not part of the graph")

    stack = Stack[GraphNode[T]]()
    stack.push(start)
    visited: Set[GraphNode[T]] = set()
    order: List[GraphNode[T]] = []

    while not stack.is_empty():
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for nbr in reversed(node.neighbours):
            if nbr not in visited:
                stack.push(nbr)

    return order