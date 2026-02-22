from dataclasses import dataclass, field
from typing import Any, Iterator, Optional
from adtlib.node import LinkedNode


@dataclass
class SinglyLinkedList:
    """
    Singly linked list ADT.

    Supports insertion, removal, and traversal in one direction (head → tail).

    :param head: First node in the list, or None if empty
    :type head: Optional[LinkedNode]
    :param tail: Last node in the list, or None if empty
    :type tail: Optional[LinkedNode]
    :param _size: Number of elements in the list
    :type _size: int
    """
    _head: Optional[LinkedNode] = field(default=None, repr=False)
    _tail: Optional[LinkedNode] = field(default=None, repr=False)
    _size: int = field(default=0, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the list.

        :return: Number of elements
        :rtype: int
        """
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over elements from head to tail.

        :return: Iterator of node values
        :rtype: Iterator[Any]
        """
        current = self.head
        while current:
            yield current.value
            current = current.next


    @property
    def head(self) -> LinkedNode:
        return self._head

    @head.setter
    def head(self, node: LinkedNode) -> None:
        self._head = node

    @property
    def tail(self) -> LinkedNode:
        return self._tail

    @tail.setter
    def tail(self, node: LinkedNode) -> None:
        self._tail = node

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, val: int) -> None:
        self._size = val


    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        :return: True if empty, False otherwise
        :rtype: bool
        """
        return self.size == 0

    def append(self, value: Any) -> None:
        """
        Add a value to the end of the list.

        :param value: Value to append
        :type value: Any
        """
        node = LinkedNode(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.add_next(node)
            self.tail = node
        self.size += 1

    def prepend(self, value: Any) -> None:
        """
        Add a value to the start of the list.

        :param value: Value to prepend
        :type value: Any
        """
        node = LinkedNode(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.add_next(self.head)
            self.head = node
        self.size += 1

    def pop_front(self) -> Any:
        """
        Remove and return the first element.

        :return: Value of the removed node
        :rtype: Any
        :raises IndexError: If the list is empty
        """
        if self.is_empty():
            raise IndexError("Pop from empty SinglyLinkedList")
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._size -= 1
        return value

    def pop_back(self) -> Any:
        """
        Remove and return the last element.

        :return: Value of the removed node
        :rtype: Any
        :raises IndexError: If the list is empty
        """
        if self.is_empty():
            raise IndexError("Pop from empty SinglyLinkedList")
        value = self.tail.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.size -= 1
        return value

    def find(self, value: Any) -> Optional[LinkedNode]:
        """
        Find the first node containing a value.

        :param value: Value to search for
        :type value: Any
        :return: Node containing the value, or None if not found
        :rtype: Optional[LinkedNode]
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None


@dataclass
class DoublyLinkedList:
    """
    Doubly linked list ADT.

    Supports insertion, removal, and traversal in both directions (head ↔ tail).

    :param head: First node in the list, or None if empty
    :type head: Optional[LinkedNode]
    :param tail: Last node in the list, or None if empty
    :type tail: Optional[LinkedNode]
    :param _size: Number of elements in the list
    :type _size: int
    """
    _head: Optional[LinkedNode] = field(default=None, repr=False)
    _tail: Optional[LinkedNode] = field(default=None, repr=False)
    _size: int = field(default=0, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the list.

        :return: Number of elements
        :rtype: int
        """
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over elements from head to tail.

        :return: Iterator of node values
        :rtype: Iterator[Any]
        """
        current = self.head
        while current:
            yield current.value
            current = current.next


    @property
    def head(self) -> Optional[LinkedNode]:
        return self._head

    @head.setter
    def head(self, node: Optional[LinkedNode]) -> None:
        self._head = node

    @property
    def tail(self) -> Optional[LinkedNode]:
        return self._tail

    @tail.setter
    def tail(self, node: Optional[LinkedNode]) -> None:
        self._tail = node

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, val: int) -> None:
        self._size = val


    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        :return: True if empty, False otherwise
        :rtype: bool
        """
        return self.size == 0

    def append(self, value: Any) -> None:
        """
        Add a value to the end of the list.

        :param value: Value to append
        :type value: Any
        """
        node = LinkedNode(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value: Any) -> None:
        """
        Add a value to the start of the list.

        :param value: Value to prepend
        :type value: Any
        """
        node = LinkedNode(value)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node
        self.size += 1

    def pop_front(self) -> Any:
        """
        Remove and return the first element.

        :return: Value of the removed node
        :rtype: Any
        :raises IndexError: If the list is empty
        """
        if self.is_empty():
            raise IndexError("Pop from empty DoublyLinkedList")
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        self.size -= 1
        return value

    def pop_back(self) -> Any:
        """
        Remove and return the last element.

        :return: Value of the removed node
        :rtype: Any
        :raises IndexError: If the list is empty
        """
        if self.is_empty():
            raise IndexError("Pop from empty DoublyLinkedList")
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return value

    def find(self, value: Any) -> Optional[LinkedNode]:
        """
        Find the first node containing a value.

        :param value: Value to search for
        :type value: Any
        :return: Node containing the value, or None if not found
        :rtype: Optional[LinkedNode]
        """
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def remove(self, node: LinkedNode) -> None:
        """
        Remove a specific node from the list.

        :param node: Node to remove
        :type node: LinkedNode
        """
        if node is self.head:
            self.pop_front()
            return

        if node is self.tail:
            self.pop_back()
            return

        # Only adjust one side per link
        node.previous.next = node.next

        # Clear node links
        node.previous = None
        node.next = None

        self.size -= 1


@dataclass
class CircularLinkedList:
    """
    Singly circular linked list ADT.

    The last node points back to the head, forming a circle.
    Supports insertion, removal, and traversal.

    :param head: First node in the list, or None if empty
    :type head: Optional[LinkedNode]
    :param tail: Last node in the list, or None if empty
    :type tail: Optional[LinkedNode]
    :param _size: Number of elements in the list
    :type _size: int
    """
    _head: Optional[LinkedNode] = field(default=None, repr=False)
    _tail: Optional[LinkedNode] = field(default=None, repr=False)
    _size: int = field(default=0, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the list.

        :return: Number of elements
        :rtype: int
        """
        return self._size

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over elements from head to tail.

        Stops after one full cycle (does not loop infinitely).

        :return: Iterator of node values
        :rtype: Iterator[Any]
        """
        current = self.head
        count = 0
        while current and count < self._size:
            yield current.value
            current = current.next
            count += 1


    @property
    def head(self) -> Optional[LinkedNode]:
        return self._head

    @head.setter
    def head(self, node: Optional[LinkedNode]) -> None:
        self._head = node

    @property
    def tail(self) -> Optional[LinkedNode]:
        return self._tail

    @tail.setter
    def tail(self, node: Optional[LinkedNode]) -> None:
        self._tail = node

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, val: int) -> None:
        self._size = val


    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        :return: True if empty, False otherwise
        :rtype: bool
        """
        return self._size == 0

    def append(self, value: Any) -> None:
        """
        Add a value to the end of the list.

        :param value: Value to append
        :type value: Any
        """
        node = LinkedNode(value)
        if self.is_empty():
            self.head = self.tail = node
            node._next = node  # points to itself
        else:
            node._next = self.head
            self.tail._next = node
            self.tail = node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """
        Add a value to the start of the list.

        :param value: Value to prepend
        :type value: Any
        """
        node = LinkedNode(value)
        if self.is_empty():
            self.head = self.tail = node
            node._next = node
        else:
            node._next = self.head
            self.tail._next = node
            self.head = node
        self._size += 1

    def pop_front(self) -> Any:
        """
        Remove and return the first element.

        :return: Value of the removed node
        :rtype: Any
        :raises IndexError: If the list is empty
        """
        if self.is_empty():
            raise IndexError("Pop from empty CircularLinkedList")
        value = self.head.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail._next = self.head
        self._size -= 1
        return value

    def pop_back(self) -> Any:
        """
        Remove and return the last element.

        :return: Value of the removed node
        :rtype: Any
        :raises IndexError: If the list is empty
        """
        if self.is_empty():
            raise IndexError("Pop from empty CircularLinkedList")
        value = self.tail.value
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current._next = self.head
            self.tail = current
        self._size -= 1
        return value

    def find(self, value: Any) -> Optional[LinkedNode]:
        """
        Find the first node containing a value.

        :param value: Value to search for
        :type value: Any
        :return: Node containing the value, or None if not found
        :rtype: Optional[LinkedNode]
        """
        current = self.head
        count = 0
        while current and count < self._size:
            if current.value == value:
                return current
            current = current.next
            count += 1
        return None