from dataclasses import dataclass, field
from typing import List, Dict, TypeVar, Generic
from adtlib.node import GraphNode


T = TypeVar("T")

@dataclass
class Graph(Generic[T]):
    """
    Graph ADT using GraphNode instances.

    Supports directed and undirected graphs, with methods for
    adding/removing nodes and edges, BFS and DFS traversal, and weighted edges.

    :param _nodes: List of all nodes in the graph
    :type _nodes: List[GraphNode]
    :param _node_map: Dictionary mapping node values to GraphNode instances
    :type _node_map: Dict[T, GraphNode[T]]
    :param _weights: Dictionary storing edge weights as (source, target) -> weight
    :type _weights: Dict[tuple[GraphNode[T], GraphNode[T]], float]
    :param _directed: Whether the graph is directed
    :type _directed: bool
    """
    _nodes: List[GraphNode[T]] = field(default_factory=list, repr=False)
    _node_map: Dict[T, GraphNode[T]] = field(default_factory=dict, repr=False)
    _weights: Dict[tuple[GraphNode[T], GraphNode[T]], float] = field(default_factory=dict, repr=False)
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
    def weights(self) -> Dict[tuple[GraphNode[T], GraphNode[T]], float]:
        """
        Get a read-only view of the graph's edge weights.

        :return: Dictionary mapping (node1, node2) tuples to edge weights
        :rtype: Dict[tuple[GraphNode, GraphNode], float]
        """
        return self._weights.copy()

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

    def add_edge(self, node1: GraphNode[T], node2: GraphNode[T], weight: float | None = None) -> None:
        """
        Add an edge between two nodes. Optionally assign a weight to the edge.

        :param node1: Source node
        :type node1: GraphNode
        :param node2: Target node
        :type node2: GraphNode
        :param weight: Optional weight for the edge
        :type weight: float | None
        :raises ValueError: If either node is not in the graph
        """
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must be part of the graph")

        node1.add_neighbour(node2)
        if not self.directed:
            node2.add_neighbour(node1)

        if weight is not None:
            self.set_edge_weight(node1, node2, weight)

    def remove_edge(self, node1: GraphNode[T], node2: GraphNode[T]) -> None:
        """
        Remove the edge between two nodes and clear any associated weight.

        :param node1: Source node
        :type node1: GraphNode
        :param node2: Target node
        :type node2: GraphNode
        :raises ValueError: If either node is not in the graph
        """
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must be part of the graph")

        node1.remove_neighbour(node2)
        self._weights.pop((node1, node2), None)

        if not self.directed:
            node2.remove_neighbour(node1)
            self._weights.pop((node2, node1), None)

    def set_edge_weight(self, node1: GraphNode[T], node2: GraphNode[T], weight: float) -> None:
        """
        Set the weight of an edge between two nodes. Automatically adds the edge if it doesn't exist.

        :param node1: Source node
        :type node1: GraphNode
        :param node2: Target node
        :type node2: GraphNode
        :param weight: Weight to assign to the edge
        :type weight: float
        :raises ValueError: If either node is not in the graph
        """
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must be part of the graph")

        self._weights[(node1, node2)] = weight
        if not self.directed:
            self._weights[(node2, node1)] = weight

    def get_edge_weight(self, node1: GraphNode[T], node2: GraphNode[T]) -> float | None:
        """
        Retrieve the weight of an edge between two nodes.

        :param node1: Source node
        :type node1: GraphNode
        :param node2: Target node
        :type node2: GraphNode
        :return: Weight of the edge if it exists, else None
        :rtype: float | None
        :raises ValueError: If either node is not in the graph
        """
        if node1 not in self.nodes or node2 not in self.nodes:
            raise ValueError("Both nodes must be part of the graph")
        
        return self._weights.get((node1, node2))
