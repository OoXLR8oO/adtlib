from dataclasses import dataclass, field
from typing import Optional, List, TypeVar, Generic
from abc import ABC, abstractmethod


T = TypeVar("T")

@dataclass
class BaseNode(ABC, Generic[T]):
    """
    Abstract base class for all node types.

    :param _value: The value stored in the node (int, float, or None)
    :type _value: int | float | None
    :param _neighbours: Get the list of neighbours connected to this node.
    :type _value: Any
    """
    _value: Optional[T] = None
    _neighbours: Optional[List[BaseNode[T]]] = field(default=None, repr=False)


    @property
    @abstractmethod
    def value(self) -> Optional[T]:
        """
        Get the value stored in this node.

        :return: The current value of the node
        :rtype: int | float | None
        """
        ...

    @value.setter
    @abstractmethod
    def value(self, val: T) -> None:
        """
        Set the value of this node.

        :param val: The value to store in the node
        :type val: int | float | None
        """
        ...

    @property
    @abstractmethod
    def neighbours(self) -> List[BaseNode[T]]:
        """
        Return a list of nodes connected to this node.
        For graphs, this is neighbours.
        For binary trees, left/right children.
        """
        ...


@dataclass(eq=False)
class GraphNode(BaseNode[T]):
    """
    Node used for graph or tree structures.

    :param _value: The value stored in the node (int, float, or None)
    :type _value: int | float | None
    :param _neighbours: List of connected nodes (edges), or None if no neighbours
    :type _neighbours: Optional[List[GraphNode]]
    """
    _neighbours: Optional[List[GraphNode[T]]] = field(default=None, repr=False)
    

    def __repr__(self) -> str:
        neigh_vals = [n.value for n in self._neighbours] if self._neighbours else []
        return f"GraphNode(value={self.value}, neighbours={neigh_vals})"

    def __hash__(self) -> int:
        return id(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GraphNode):
            return NotImplemented
        return id(self) == id(other)


    @property
    def value(self) -> T:
        """
        Get the value stored in this graph node.

        :return: The current value of the node
        :rtype: int | float | None
        """
        return self._value

    @value.setter
    def value(self, val: T) -> None:
        """
        Set the value stored in this graph node.

        :param val: The value to store
        :type val: int | float | None
        """
        self._value = val

    @property
    def neighbours(self) -> List[GraphNode[T]]:
        """
        Get the list of neighbours connected to this node.
        This returns a shallow copy with `.copy()`. External
        mutations will not affect the internal list, but mutating 
        the values in this list will affect the class' internal list.

        :return: List of neighbour nodes (or an empty list)
        :rtype: List[GraphNode]
        """
        if self._neighbours is None:
            return []
        return self._neighbours.copy()

    @neighbours.setter
    def neighbours(self, val: Optional[List[GraphNode[T]]]) -> None:
        """
        Set the neighbours list.

        :param val: List of nodes to assign as neighbours
        :type val: Optional[List[GraphNode]]
        """
        self._neighbours = val


    def add_neighbour(self, node: GraphNode[T]) -> None:
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

    def remove_neighbour(self, node: GraphNode[T]) -> None:
        """
        Remove a neighbour node from this node.

        :param node: Node to remove
        :type node: GraphNode
        """
        if not self._neighbours:
            return

        if node in self._neighbours:
            self._neighbours.remove(node)

    def detach_neighbours(self) -> None:
        """
        Remove all neighbours from this node.
        """
        self._neighbours = []

    def has_neighbour(self, node: GraphNode[T]) -> bool:
        """Check if a given node is a neighbour."""
        return node in self._neighbours if self._neighbours else False

    def degree(self) -> int:
        """
        Return the number of neighbours (outgoing edges).

        :return: Number of neighbours
        :rtype: int
        """
        return len(self._neighbours) if self._neighbours else 0


@dataclass
class LinkedNode(BaseNode[T]):
    """
    Node used for linked list structures.

    :param _value: The value stored in the node (int, float, or None)
    :type _value: int | float | None
    :param _previous: Previous linked node or None
    :type _previous: Optional[LinkedNode]
    :param _next: Next linked node or None
    :type _next: Optional[LinkedNode]
    """
    _previous: Optional[LinkedNode[T]] = field(default=None, repr=False)
    _next: Optional[LinkedNode[T]] = field(default=None, repr=False)


    def __repr__(self) -> str:
        prev_val = self.previous.value if self.previous else None
        next_val = self.next.value if self.next else None
        return f"LinkedNode(value={self.value}, prev={prev_val}, next={next_val})"


    @property
    def value(self) -> T:
        """
        Get the value stored in this linked node.

        :return: The current value of the node
        :rtype: int | float | None
        """
        return self._value

    @value.setter
    def value(self, val: T) -> None:
        """
        Set the value stored in this linked node.

        :param val: The value to store
        :type val: int | float | None
        """
        self._value = val

    @property
    def previous(self) -> Optional[LinkedNode[T]]:
        """
        Get the previous linked node.

        :return: The previous node or None
        :rtype: Optional[LinkedNode]
        """
        return self._previous

    @previous.setter
    def previous(self, node: Optional[LinkedNode[T]]) -> None:
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
    def next(self) -> Optional[LinkedNode[T]]:
        """
        Get the next linked node.

        :return: The next node or None
        :rtype: Optional[LinkedNode]
        """
        return self._next

    @next.setter
    def next(self, node: Optional[LinkedNode[T]]) -> None:
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

    @property
    def neighbours(self) -> List[BaseNode[T]]:
        return [n for n in (self.next,) if n is not None]  # linear chain
            

    def add_previous(self, node: LinkedNode[T]) -> None:
        """
        Attach a node before this one.

        :param node: Node to link as previous
        :type node: LinkedNode
        """
        self.previous = node

    def add_next(self, node: LinkedNode[T]) -> None:
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


@dataclass
class TreeNode(BaseNode[T]):
    """
    Node used for binary tree structures.

    :param _value: The value stored in the node (int, float, or None)
    :type _value: int | float | None
    :param _left: Left child node or None
    :type _left: Optional[TreeNode]
    :param _right: Right child node or None
    :type _right: Optional[TreeNode]
    :param _parent: Parent node or None
    :type _parent: Optional[TreeNode]
    """
    _left: Optional[TreeNode[T]] = field(default=None, repr=False)
    _right: Optional[TreeNode[T]] = field(default=None, repr=False)
    _parent: Optional[TreeNode[T]] = field(default=None, repr=False)


    def __repr__(self) -> str:
        left_val = self.left.value if self.left else None
        right_val = self.right.value if self.right else None
        return f"TreeNode(value={self.value}, left={left_val}, right={right_val})"


    @property
    def value(self) -> T:
        """
        Get the value stored in this tree node.

        :return: The current value of the node
        :rtype: int | float | None
        """
        return self._value

    @value.setter
    def value(self, val: T) -> None:
        """
        Set the value stored in this tree node.

        :param val: The value to store
        :type val: int | float | None
        """
        self._value = val

    @property
    def left(self) -> Optional[TreeNode[T]]:
        """
        Get the left child node.

        :return: The left child or None
        :rtype: Optional[TreeNode]
        """
        return self._left

    @left.setter
    def left(self, node: Optional[TreeNode[T]]) -> None:
        """
        Set the left child node.

        :param node: Node to assign as left child
        :type node: Optional[TreeNode]
        :raises ValueError: If attempting to assign the node to itself
        """
        if node is self:
            raise ValueError("A node cannot be its own child")

        if self._left:
            self._left._parent = None

        self._left = node

        if node:
            node._parent = self

    @property
    def right(self) -> Optional[TreeNode[T]]:
        """
        Get the right child node.

        :return: The right child or None
        :rtype: Optional[TreeNode]
        """
        return self._right

    @right.setter
    def right(self, node: Optional[TreeNode[T]]) -> None:
        """
        Set the right child node.

        :param node: Node to assign as right child
        :type node: Optional[TreeNode]
        :raises ValueError: If attempting to assign the node to itself
        """
        if node is self:
            raise ValueError("A node cannot be its own child")

        if self._right:
            self._right._parent = None

        self._right = node

        if node:
            node._parent = self

    @property
    def parent(self) -> Optional[TreeNode]:
        """
        Get the parent node.

        :return: The parent node or None
        :rtype: Optional[TreeNode]
        """
        return self._parent

    @property
    def neighbours(self) -> List[BaseNode[T]]:
        return [child for child in (self.left, self.right) if child is not None]


    def is_leaf(self) -> bool:
        """
        Determine whether this node is a leaf node.

        :return: True if the node has no children, otherwise False
        :rtype: bool
        """
        return self._left is None and self._right is None