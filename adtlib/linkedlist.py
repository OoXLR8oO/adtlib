from dataclasses import dataclass, field
from collections.abc import Iterator
from adtlib.node import LinkedNode


@dataclass
class SinglyLinkedList[T]:
    """
    Singly linked list ADT.

    Supports insertion, removal, and traversal in one direction (head → tail).

    :param head: First node in the list, or None if empty
    :type head: LinkedNode[T] | None
    :param tail: Last node in the list, or None if empty
    :type tail: LinkedNode[T] | None
    :param _size: Number of elements in the list
    :type _size: int
    """
    _head: LinkedNode[T] | None = field(default=None, init=False, repr=False)
    _tail: LinkedNode[T] | None = field(default=None, init=False, repr=False)
    _size: int = field(default=0, init=False, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the list.

        :return: Number of elements
        :rtype: int
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over elements from head to tail.

        :return: Iterator of node values
        :rtype: Iterator[T]
        """
        current = self._head
        while current:
            yield current.value
            current = current.next


    @property
    def head(self) -> LinkedNode[T] | None:
        return self._head

    @head.setter
    def head(self, node: LinkedNode[T] | None) -> None:
        self._head = node

    @property
    def tail(self) -> LinkedNode[T] | None:
        return self._tail

    @tail.setter
    def tail(self, node: LinkedNode[T] | None) -> None:
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

    def append(self, value: T) -> None:
        """
        Add a value to the end of the list.

        :param value: Value to append
        :type value: T
        """
        node = LinkedNode(value)

        if self._head is None:
            self._head = self._tail = node
        else:
            assert self._tail is not None
            self._tail.next = node
            self._tail = node

        self._size += 1

    def prepend(self, value: T) -> None:
        """
        Add a value to the start of the list.

        :param value: Value to prepend
        :type value: T
        """
        node = LinkedNode(value)

        if self._head is None:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head = node

        self._size += 1

    def pop_front(self) -> T:
        """
        Remove and return the first element.

        :return: Value of the removed node
        :rtype: T
        :raises IndexError: If the list is empty
        """
        if self._head is None:
            raise IndexError("Pop from empty SinglyLinkedList")

        value = self._head.value
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self._size -= 1
        return value

    def pop_back(self) -> T:
        """
        Remove and return the last element.

        :return: Value of the removed node
        :rtype: T
        :raises IndexError: If the list is empty
        """
        if self._tail is None:
            raise IndexError("Pop from empty SinglyLinkedList")

        value = self._tail.value

        if self._head is self._tail:
            self._head = self._tail = None
        else:
            current = self._head
            while current.next is not self._tail:
                current = current.next

            current.next = None
            self._tail = current

        self._size -= 1
        return value

    def find(self, value: T) -> LinkedNode[T] | None:
        """
        Find the first node containing a value.

        :param value: Value to search for
        :type value: T
        :return: Node containing the value, or None if not found
        :rtype: LinkedNode | None
        """
        current = self._head

        while current:
            if current.value == value:
                return current
            current = current.next

        return None


@dataclass
class DoublyLinkedList[T]:
    """
    Doubly linked list ADT.

    Supports insertion, removal, and traversal in both directions (head ↔ tail).

    :param head: First node in the list, or None if empty
    :type head: LinkedNode | None
    :param tail: Last node in the list, or None if empty
    :type tail: LinkedNode | None
    :param _size: Number of elements in the list
    :type _size: int
    """
    _head: LinkedNode[T] | None = field(default=None, init=False, repr=False)
    _tail: LinkedNode[T] | None = field(default=None, init=False, repr=False)
    _size: int = field(default=0, init=False, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the list.

        :return: Number of elements
        :rtype: int
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over elements from head to tail.

        :return: Iterator of node values
        :rtype: Iterator[T]
        """
        current = self._head
        while current:
            yield current.value
            current = current.next


    @property
    def head(self) -> LinkedNode[T] | None:
        return self._head

    @head.setter
    def head(self, node: LinkedNode[T] | None) -> None:
        self._head = node

    @property
    def tail(self) -> LinkedNode[T] | None:
        return self._tail

    @tail.setter
    def tail(self, node: LinkedNode[T] | None) -> None:
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

    def append(self, value: T) -> None:
        """
        Add a value to the end of the list.

        :param value: Value to append
        :type value: T
        """
        node = LinkedNode(value)

        if self._head is None:
            self._head = self._tail = node
        else:
            assert self._tail is not None
            node.previous = self._tail
            self._tail.next = node
            self._tail = node

        self._size += 1

    def prepend(self, value: T) -> None:
        """
        Add a value to the start of the list.

        :param value: Value to prepend
        :type value: T
        """
        node = LinkedNode(value)

        if self._head is None:
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head.previous = node
            self._head = node

        self._size += 1

    def pop_front(self) -> T:
        """
        Remove and return the first element.

        :return: Value of the removed node
        :rtype: T
        :raises IndexError: If the list is empty
        """
        if self._head is None:
            raise IndexError("Pop from empty DoublyLinkedList")

        value = self._head.value
        self._head = self._head.next

        if self._head:
            self._head.previous = None
        else:
            self._tail = None

        self._size -= 1
        return value

    def pop_back(self) -> T:
        """
        Remove and return the last element.

        :return: Value of the removed node
        :rtype: T
        :raises IndexError: If the list is empty
        """
        if self._tail is None:
            raise IndexError("Pop from empty DoublyLinkedList")

        value = self._tail.value
        self._tail = self._tail.previous

        if self._tail:
            self._tail.next = None
        else:
            self._head = None

        self._size -= 1
        return value

    def find(self, value: T) -> LinkedNode[T] | None:
        """
        Find the first node containing a value.

        :param value: Value to search for
        :type value: T
        :return: Node containing the value, or None if not found
        :rtype: Optional[LinkedNode]
        """
        current = self._head

        while current:
            if current.value == value:
                return current
            current = current.next

        return None

    def remove(self, node: LinkedNode[T]) -> None:
        """
        Remove a specific node from the list.

        :param node: Node to remove
        :type node: LinkedNode
        """
        if node is self._head:
            self.pop_front()
            return

        if node is self._tail:
            self.pop_back()
            return

        prev_node = node.previous
        next_node = node.next

        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.previous = prev_node

        node.previous = None
        node.next = None

        self._size -= 1


@dataclass
class CircularLinkedList[T]:
    """
    Singly circular linked list ADT.

    The last node points back to the head, forming a circle.
    Supports insertion, removal, and traversal.

    :param _head: First node in the list, or None if empty
    :type _head: LinkedNode | None
    :param _tail: Last node in the list, or None if empty
    :type _tail: LinkedNode | None
    :param _size: Number of elements in the list
    :type _size: int
    """
    _head: LinkedNode[T] | None = field(default=None, init=False, repr=False)
    _tail: LinkedNode[T] | None = field(default=None, init=False, repr=False)
    _size: int = field(default=0, init=False, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the list.

        :return: Number of elements
        :rtype: int
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over elements from head to tail.

        :return: Iterator of node values
        :rtype: Iterator[T]
        """
        current = self._head
        count = 0

        while current and count < self._size:
            yield current.value
            current = current.next
            count += 1


    @property
    def head(self) -> LinkedNode[T] | None:
        return self._head

    @head.setter
    def head(self, node: LinkedNode[T] | None) -> None:
        self._head = node

    @property
    def tail(self) -> LinkedNode[T] | None:
        return self._tail

    @tail.setter
    def tail(self, node: LinkedNode[T] | None) -> None:
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

    def append(self, value: T) -> None:
        """
        Add a value to the end of the list.

        :param value: Value to append
        :type value: T
        """
        node = LinkedNode(value)

        if self._head is None:
            self._head = self._tail = node
            node.next = node
        else:
            assert self._tail is not None

            if node is self._head or node is self._tail:
                raise ValueError("Cannot append a node that would self-link improperly.")

            node.next = self._head
            self._tail.next = node
            self._tail = node

        self._size += 1

    def prepend(self, value: T) -> None:
        """
        Add a value to the start of the list.

        :param value: Value to prepend
        :type value: T
        """
        node = LinkedNode(value)

        if self._head is None:
            self._head = self._tail = node
            node.next = node
        else:
            assert self._tail is not None

            if node is self._head or node is self._tail:
                raise ValueError("Cannot append a node that would self-link improperly.")

            node.next = self._head
            self._tail.next = node
            self._head = node

        self._size += 1

    def pop_front(self) -> T:
        """
        Remove and return the first element.

        :return: Value of the removed node
        :rtype: T
        :raises IndexError: If the list is empty
        """
        if self._head is None:
            raise IndexError("Pop from empty CircularLinkedList")

        value = self._head.value

        if self._head is self._tail:
            self._head = self._tail = None
        else:
            assert self._tail is not None
            self._head = self._head.next
            self._tail.next = self._head

        self._size -= 1
        return value

    def pop_back(self) -> T:
        """
        Remove and return the last element.

        :return: Value of the removed node
        :rtype: T
        :raises IndexError: If the list is empty
        """
        if self._tail is None:
            raise IndexError("Pop from empty CircularLinkedList")

        value = self._tail.value

        if self._head is self._tail:
            self._head = self._tail = None
        else:
            current = self._head
            while current.next is not self._tail:
                current = current.next

            current.next = self._head
            self._tail = current

        self._size -= 1
        return value

    def find(self, value: T) -> LinkedNode[T] | None:
        """
        Find the first node containing a value.

        :param value: Value to search for
        :type value: T
        :return: Node containing the value, or None if not found
        :rtype: Optional[LinkedNode]
        """
        current = self._head
        count = 0

        while current and count < self._size:
            if current.value == value:
                return current

            current = current.next
            count += 1

        return None

    def remove(self, node: LinkedNode[T]) -> None:
        """
        Remove a specific node from the list.

        :param node: Node to remove
        :type node: LinkedNode
        """
        if self._head is None:
            raise ValueError("Remove from empty CircularLinkedList")

        # Removing head
        if node is self._head:
            self.pop_front()
            return

        # Removing tail
        if node is self._tail:
            self.pop_back()
            return

        # Removing middle node
        current = self._head

        while current.next is not node:
            current = current.next

            if current is self._head:
                raise ValueError("Node not found in list")

        current.next = node.next
        node.next = None

        self._size -= 1