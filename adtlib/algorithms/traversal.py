from adtlib.graph import Graph
from adtlib.node import GraphNode
from adtlib.queue import Queue, PriorityQueue
from adtlib.stack import Stack


def bfs(graph: Graph, start: GraphNode) -> list[GraphNode]:
    """
    Perform breadth-first search within a graph starting from a node.

    :param graph: Graph containing nodes
    :type graph: Graph
    :param start: Node to start traversal from
    :type start: GraphNode
    :return: List of nodes in BFS order
    :rtype: list[GraphNode]
    :raises ValueError: If the start node is not part of the graph
    """
    if start not in graph.nodes:
        raise ValueError("Start node is not part of the graph")

    queue = Queue()
    queue.enqueue(start)
    visited: set[GraphNode] = set()
    order: list[GraphNode] = []

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


def dfs(graph: Graph, start: GraphNode) -> list[GraphNode]:
    """
    Perform depth-first search within a graph starting from a node.

    :param graph: Graph containing nodes
    :type graph: Graph
    :param start: Node to start traversal from
    :type start: GraphNode
    :return: List of nodes in DFS order
    :rtype: list[GraphNode]
    :raises ValueError: If the start node is not part of the graph
    """
    if start not in graph.nodes:
        raise ValueError("Start node is not part of the graph")

    stack = Stack()
    stack.push(start)
    visited: set[GraphNode] = set()
    order: list[GraphNode] = []

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


def dijkstra(graph: Graph, start: GraphNode) -> tuple[dict[GraphNode, float], dict[GraphNode, GraphNode]]:
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
    distances: dict[GraphNode, float] = {node: float('inf') for node in graph.nodes}
    previous: dict[GraphNode, GraphNode] = {}
    distances[start] = 0

    pq = PriorityQueue[GraphNode]()
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