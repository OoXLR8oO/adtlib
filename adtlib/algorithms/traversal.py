from typing import Dict, List, TypeVar, Tuple, Set
from heapq import heappush, heappop
from adtlib.graph import Graph
from adtlib.node import GraphNode
from adtlib.queue import PriorityQueue, Queue
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


# def dijkstra(graph: Graph[T], start: GraphNode[T]) -> Tuple[Dict[GraphNode[T], float], Dict[GraphNode[T], GraphNode[T]]]:
#     """
#     Compute shortest paths from the start node to all other nodes using Dijkstra's algorithm.

#     :param graph: Graph instance containing nodes and weighted edges
#     :param start: Node to start traversal from
#     :return: Tuple of (distances, previous) dictionaries:
#              - distances[node] = shortest distance from start
#              - previous[node] = previous node along shortest path
#     :raises ValueError: If start node is not part of the graph
#     """
#     if start not in graph.nodes:
#         raise ValueError("Start node is not part of the graph")

#     # Initialize distances to infinity
#     distances: Dict[GraphNode[T], float] = {node: float('inf') for node in graph.nodes}
#     previous: Dict[GraphNode[T], GraphNode[T]] = {}

#     distances[start] = 0
#     heap: List[Tuple[float, GraphNode[T]]] = [(0, start)]

#     while heap:
#         current_dist, node = heappop(heap)

#         # Skip if we already have a shorter distance recorded
#         if current_dist > distances[node]:
#             continue

#         for neighbor in node.neighbours:
#             weight = graph.get_edge_weight(node, neighbor)
#             if weight is None:
#                 continue  # Skip edges without a weight

#             distance = current_dist + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 previous[neighbor] = node
#                 heappush(heap, (distance, neighbor))

#     return distances, previous

# def shortest_path(previous: Dict[GraphNode[T], GraphNode[T]], start: GraphNode[T], end: GraphNode[T]) -> List[GraphNode[T]]:
#     """
#     Reconstruct the shortest path from start to end using the previous dictionary.

#     :param previous: Dictionary mapping node to its predecessor in the shortest path
#     :param start: Start node
#     :param end: End node
#     :return: List of nodes representing the shortest path from start to end
#     """
#     path: List[GraphNode[T]] = []
#     current = end

#     while current != start:
#         path.append(current)
#         if current not in previous:
#             return []  # No path exists
#         current = previous[current]

#     path.append(start)
#     path.reverse()
#     return path

def dijkstra(graph: Graph[T], start: GraphNode[T]) -> Tuple[Dict[GraphNode[T], float], Dict[GraphNode[T], GraphNode[T]]]:
    """
        Compute shortest paths from the start node to all other nodes using Dijkstra's algorithm.

        :param graph: Graph instance containing nodes and weighted edges
        :param start: Node to start traversal from
        :return: Tuple of two dictionaries:
                - distances[node] = shortest distance from start
                - previous[node] = previous node along shortest path
        :raises ValueError: If start node is not part of the graph
        """
    if start not in graph.nodes:
        raise ValueError("Start node is not part of the graph")

    # Initialize distances to infinity
    distances: Dict[GraphNode[T], float] = {node: float('inf') for node in graph.nodes}
    previous: Dict[GraphNode[T], GraphNode[T]] = {}
    distances[start] = 0

    # Use your PriorityQueue ADT (min-priority by distance)
    pq = PriorityQueue[GraphNode[T]]()
    pq.push(start, 0)

    while not pq.is_empty():
        current = pq.pop()
        current_dist = distances[current]

        for neighbor in current.neighbours:
            # Get edge weight; if none, skip
            weight = graph.get_edge_weight(current, neighbor)
            if weight is None:
                continue

            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current
                pq.push(neighbor, distance)

    return distances, previous