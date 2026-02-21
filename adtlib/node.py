from dataclasses import dataclass, field
from typing import Optional, List
from abc import ABC, abstractmethod


@dataclass
class BaseNode(ABC):
    """
    Abstract base class for all node types.

    :param _value: The value stored in the node (int, float, or None)
    :type _value: int | float | None
    """
    _value: int | float | None = None


    @property
    @abstractmethod
    def value(self) -> int | float | None:
        """
        Get the value stored in this node.

        :return: The current value of the node
        :rtype: int | float | None
        """
        ...

    @value.setter
    @abstractmethod
    def value(self, val) -> None:
        """
        Set the value of this node.

        :param val: The value to store in the node
        :type val: int | float | None
        """
        ...


@dataclass
class GraphNode(BaseNode):
    """
    Node used for graph or tree structures.

    :param _value: The value stored in the node (int, float, or None)
    :type _value: int | float | None
    :param _neighbours: List of connected nodes (edges), or None if no neighbours
    :type _neighbours: Optional[List[GraphNode]]
    """
    _neighbours: Optional[List[GraphNode]] = field(default=None, repr=False)
    

    def __repr__(self):
        neigh_vals = [n.value for n in self._neighbours] if self._neighbours else []
        return f"GraphNode(value={self.value}, neighbours={neigh_vals})"


    @property
    def value(self) -> int | float | None:
        """
        Get the value stored in this graph node.

        :return: The current value of the node
        :rtype: int | float | None
        """
        return self._value

    @value.setter
    def value(self, val) -> None:
        """
        Set the value stored in this graph node.

        :param val: The value to store
        :type val: int | float | None
        """
        self._value = val

    @property
    def neighbours(self) -> Optional[List[GraphNode]]:
        """
        Get the list of neighbours connected to this node.

        :return: List of neighbour nodes or None
        :rtype: Optional[List[GraphNode]]
        """
        return self._neighbours

    @neighbours.setter
    def neighbours(self, val: Optional[List[GraphNode]]) -> None:
        """
        Set the neighbours list.

        :param val: List of nodes to assign as neighbours
        :type val: Optional[List[GraphNode]]
        """
        self._neighbours = val


    def add_neighbour(self, node: GraphNode) -> None:
        """
        Add a directed edge from this node to another node.

        :param node: Node to connect to
        :type node: GraphNode
        :raises ValueError: If attempting to connect the node to itself
        """
        if node is self:
            raise ValueError("A node cannot be its own neighbour")

        if self._neighbours is None:
            self._neighbours = []

        if node not in self._neighbours:
            self._neighbours.append(node)

    def remove_neighbour(self, node: GraphNode) -> None:
        """
        Remove a neighbour node from this node.

        :param node: Node to remove
        :type node: GraphNode
        """
        if not self._neighbours:
            return

        if node in self._neighbours:
            self._neighbours.remove(node)

        if not self._neighbours:
            self._neighbours = None

    def detach_neighbours(self) -> None:
        """
        Remove all neighbours from this node.
        """
        self._neighbours = None

    def degree(self) -> int:
        """
        Return the number of neighbours (outgoing edges).

        :return: Number of neighbours
        :rtype: int
        """
        return len(self._neighbours) if self._neighbours else 0


@dataclass
class LinkedNode(BaseNode):
    """
    Node used for linked list structures.

    :param _value: The value stored in the node (int, float, or None)
    :type _value: int | float | None
    :param _previous: Previous linked node or None
    :type _previous: Optional[LinkedNode]
    :param _next: Next linked node or None
    :type _next: Optional[LinkedNode]
    """
    _previous: Optional[LinkedNode] = field(default=None, repr=False)
    _next: Optional[LinkedNode] = field(default=None, repr=False)


    def __repr__(self):
        prev_val = self.previous.value if self.previous else None
        next_val = self.next.value if self.next else None
        return f"LinkedNode(value={self.value}, prev={prev_val}, next={next_val})"


    @property
    def value(self) -> int | float | None:
        """
        Get the value stored in this linked node.

        :return: The current value of the node
        :rtype: int | float | None
        """
        return self._value

    @value.setter
    def value(self, val) -> None:
        """
        Set the value stored in this linked node.

        :param val: The value to store
        :type val: int | float | None
        """
        self._value = val

    @property
    def previous(self) -> Optional[LinkedNode]:
        """
        Get the previous linked node.

        :return: The previous node or None
        :rtype: Optional[LinkedNode]
        """
        return self._previous

    @previous.setter
    def previous(self, node: Optional[LinkedNode]) -> None:
        """
        Set the previous node in the linked list.

        :param node: Node to link as previous
        :type node: Optional[LinkedNode]
        :raises ValueError: If attempting to link the node to itself
        """
        if node is self:
            raise ValueError("A node cannot link to itself")

        if self._previous and self._previous._next is self:
            self._previous._next = None

        self._previous = node

        if node and node._next is not self:
            node._next = self

    @property
    def next(self) -> Optional[LinkedNode]:
        """
        Get the next linked node.

        :return: The next node or None
        :rtype: Optional[LinkedNode]
        """
        return self._next

    @next.setter
    def next(self, node: Optional[LinkedNode]) -> None:
        """
        Set the next node in the linked list.

        :param node: Node to link as next
        :type node: Optional[LinkedNode]
        :raises ValueError: If attempting to link the node to itself
        """
        if node is self:
            raise ValueError("A node cannot link to itself")

        if self._next and self._next._previous is self:
            self._next._previous = None

        self._next = node

        if node and node._previous is not self:
            node._previous = self
            

    def add_previous(self, node: LinkedNode) -> None:
        """
        Attach a node before this one.

        :param node: Node to link as previous
        :type node: LinkedNode
        """
        self.previous = node

    def add_next(self, node: LinkedNode) -> None:
        """
        Attach a node after this one.

        :param node: Node to link as next
        :type node: LinkedNode
        """
        self.next = node

    def detach(self) -> None:
        """
        Fully unlink this node from its previous and next neighbours.
        """
        if self._previous: self._previous._next = None
        if self._next: self._next._previous = None
        self._previous = self._next = None