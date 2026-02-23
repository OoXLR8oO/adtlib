from dataclasses import dataclass, field
from typing import Any, List, Set, Dict, TypeVar, Generic
from adtlib.node import GraphNode
from adtlib.queue import Queue
from adtlib.stack import Stack


T = TypeVar("T")

@dataclass
class Graph(Generic[T]):
    """
    Graph ADT using GraphNode instances.

    Supports directed and undirected graphs, with methods for
    adding/removing nodes and edges, as well as BFS and DFS traversal.

    :param _nodes: List of all nodes in the graph
    :type _nodes: List[GraphNode]
    :param _directed: Whether the graph is directed
    :type _directed: bool
    """
    _nodes: List[GraphNode[T]] = field(default_factory=list, repr=False)
    _node_map: Dict[T, GraphNode[T]] = field(default_factory=dict, repr=False)
    _directed: bool = False

    @property
    def nodes(self) -> List[GraphNode[T]]:
        """
        Get the list of all nodes in the graph.

        :return: List of GraphNode instances
        :rtype: List[GraphNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, value: List[GraphNode[T]]) -> None:
        """
        Set the list of nodes in the graph.

        :param value: List of GraphNode instances
        :type value: List[GraphNode]
        """
        self._nodes = value
        self._node_map = {node.value: node for node in value}

    @property
    def directed(self) -> bool:
        """
        Get whether the graph is directed.

        :return: True if directed, False otherwise
        :rtype: bool
        """
        return self._directed

    @directed.setter
    def directed(self, value: bool) -> None:
        """
        Set whether the graph is directed.

        :param value: True for directed, False for undirected
        :type value: bool
        """
        self._directed = value

    def add_node(self, node: GraphNode[T]) -> None:
        """
        Add a new GraphNode to the graph.

        :param node: GraphNode instance to add
        :type node: GraphNode
        """
        if node.value in self._node_map:
            return
        self._nodes.append(node)
        self._node_map[node.value] = node

    def get_node(self, value: T) -> GraphNode[T] | None:
        return self._node_map.get(value)

    def remove_node(self, node: GraphNode[T]) -> None:
        """
        Remove a node and all edges to/from it.

        :param node: Node to remove
        :type node: GraphNode
        """
        for n in self.nodes:
            n.neighbours = [nbr for nbr in n.neighbours if nbr is not node]
        if node in self.nodes:
            self.nodes.remove(node)
        if node.value in self._node_map:
            del self._node_map[node.value]

    def add_edge(self, node1: GraphNode[T], node2: GraphNode[T]) -> None:
        """
        Add an edge between two nodes.

        :param node1: Source node
        :type node1: GraphNode
        :param node2: Target node
        :type node2: GraphNode
        """
        node1.add_neighbour(node2)
        if not self.directed:
            node2.add_neighbour(node1)

    def remove_edge(self, node1: GraphNode[T], node2: GraphNode[T]) -> None:
        """
        Remove the edge between two nodes.

        :param node1: Source node
        :type node1: GraphNode
        :param node2: Target node
        :type node2: GraphNode
        """
        node1.remove_neighbour(node2)
        if not self.directed:
            node2.remove_neighbour(node1)

    def bfs(self, start: GraphNode[T]) -> List[T]:
        """
        Perform breadth-first search starting from a node.

        :param start: Starting node
        :type start: GraphNode
        :return: List of node values in BFS order
        :rtype: List[GraphNode]
        """
        queue = Queue[GraphNode[T]]()
        queue.enqueue(start)
        visited: Set[GraphNode[T]] = set()
        order: List[T] = []
        while not queue.is_empty():
            node = queue.dequeue()
            if node in visited:
                continue
            visited.add(node)
            order.append(node.value)
            for nbr in node.neighbours:
                if nbr not in visited:
                    queue.enqueue(nbr)
        return order

    def dfs(self, start: GraphNode[T]) -> List[T]:
        """
        Perform depth-first search starting from a node.

        :param start: Starting node
        :type start: GraphNode
        :return: List of node values in DFS order
        :rtype: List[GraphNode]
        """
        visited: Set[GraphNode[T]] = set()
        stack = Stack[GraphNode[T]]()
        stack.push(start)
        order: List[T] = []

        while not stack.is_empty():
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node.value)
            for nbr in reversed(node.neighbours):
                if nbr not in visited:
                    stack.push(nbr)
        return order