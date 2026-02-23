from dataclasses import dataclass, field
from typing import Iterator, Iterable, Tuple, TypeVar, Generic
from collections import deque
import heapq
from itertools import count


T = TypeVar("T")

@dataclass
class Queue(Generic[T]):
    """
    First-in, first-out (FIFO) queue.

    A simple queue ADT with methods to enqueue, dequeue, peek, and check if empty.

    :param _data: Internal storage for queue items
    :type _data: deque[Any]
    """
    _data: deque[T] = field(default_factory=deque, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the queue.

        :return: Number of items currently in the queue
        :rtype: int
        """
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over items from front to back.

        :return: Iterator yielding items in enqueue order
        :rtype: Iterator[Any]
        """
        return iter(self._data)

    def __reversed__(self) -> Iterator[T]:
        """
        Iterate over items from back to front.

        :return: Reverse iterator yielding items
        :rtype: Iterator[Any]
        """
        return reversed(self._data)

    def __repr__(self) -> str:
        """
        Return a string representation of the queue.

        :return: Human-readable string showing queue contents
        :rtype: str
        """
        return f"Queue({list(self._data)!r})"


    @property
    def data(self) -> Iterable[T]:
        """
        Return a read-only view of the queue contents.

        :return: Iterable of items currently in the queue
        :rtype: Iterable[Any]
        """
        return self._data


    def enqueue(self, item: T) -> None:
        """
        Add an item to the back of the queue.

        :param item: Item to add to the queue
        :type item: Any
        """
        self._data.append(item)

    def dequeue(self) -> T:
        """
        Remove and return the front item from the queue.

        :return: The earliest enqueued item
        :rtype: Any
        :raises IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty Queue")
        return self._data.popleft()

    def peek(self) -> T:
        """
        Return the front item without removing it.

        :return: The earliest enqueued item
        :rtype: Any
        :raises IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek from empty Queue")
        return self._data[0]

    def is_empty(self) -> bool:
        """
        Check whether the queue contains any items.

        :return: True if the queue is empty, False otherwise
        :rtype: bool
        """
        return not self._data

    def clear(self) -> None:
        """Remove all items from the queue."""
        self._data.clear()


@dataclass
class Deque(Generic[T]):
    """
    Double-ended queue (Deque).

    A deque ADT supporting insertion and removal of elements
    from both the front and the back.

    :param _data: Internal storage for deque items
    :type _data: deque[Any]
    """
    _data: deque[T] = field(default_factory=deque, repr=False)


    def __len__(self) -> int:
        """
        Return the number of items in the deque.

        :return: Number of items currently stored
        :rtype: int
        """
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over items from front to back.

        :return: Iterator yielding items from front to back
        :rtype: Iterator[Any]
        """
        return iter(self._data)

    def __reversed__(self) -> Iterator[T]:
        """
        Iterate over items from back to front.

        :return: Reverse iterator yielding items
        :rtype: Iterator[Any]
        """
        return reversed(self._data)

    def __repr__(self) -> str:
        """
        Return a string representation of the deque.

        :return: Human-readable string showing deque contents
        :rtype: str
        """
        return f"Deque({list(self._data)!r})"


    @property
    def data(self) -> Iterable[T]:
        """
        Return a read-only view of the deque contents.

        :return: Iterable of items currently stored
        :rtype: Iterable[Any]
        """
        return self._data


    def append(self, item: T) -> None:
        """
        Add an item to the back of the deque.

        :param item: Item to add
        :type item: Any
        """
        self._data.append(item)

    def append_left(self, item: T) -> None:
        """
        Add an item to the front of the deque.

        :param item: Item to add
        :type item: Any
        """
        self._data.appendleft(item)

    def pop(self) -> T:
        """
        Remove and return the back item.

        :return: The last item
        :rtype: Any
        :raises IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty Deque")
        return self._data.pop()

    def pop_left(self) -> T:
        """
        Remove and return the front item.

        :return: The first item
        :rtype: Any
        :raises IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop_left from empty Deque")
        return self._data.popleft()

    def peek_front(self) -> T:
        """
        Return the front item without removing it.

        :return: The first item
        :rtype: Any
        :raises IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek_front from empty Deque")
        return self._data[0]

    def peek_back(self) -> T:
        """
        Return the back item without removing it.

        :return: The last item
        :rtype: Any
        :raises IndexError: If the deque is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek_back from empty Deque")
        return self._data[-1]

    def is_empty(self) -> bool:
        """
        Check whether the deque contains any items.

        :return: True if the deque is empty, False otherwise
        :rtype: bool
        """
        return not self._data

    def clear(self) -> None:
        """Remove all items from the deque."""
        self._data.clear()


@dataclass
class PriorityQueue(Generic[T]):
    """
    Priority queue where each element has a priority.

    Items are retrieved in order of priority (lowest number = highest priority).

    :param _data: Internal storage as a min-heap of tuples (priority, counter, item)
    :type _data: list[Tuple[int, int, Any]]
    """
    _data: list[Tuple[int, int, T]] = field(default_factory=list, repr=False)
    _counter: count = field(default_factory=count, init=False, repr=False)

    def __len__(self) -> int:
        """
        Return the number of items in the priority queue.

        :return: Number of items currently stored
        :rtype: int
        """
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over items by heap order (not strictly priority order).

        :return: Iterator yielding items in heap order
        :rtype: Iterator[Any]
        """
        return (item for _, _, item in self._data)

    def __repr__(self) -> str:
        """
        Return a string representation of the priority queue.

        :return: Human-readable string showing queue contents with priorities
        :rtype: str
        """
        return f"PriorityQueue({self._data!r})"

    def push(self, item: T, priority: int) -> None:
        """
        Add an item with a given priority.

        :param item: Item to add
        :type item: Any
        :param priority: Priority of the item (lower = higher priority)
        :type priority: int
        """
        heapq.heappush(self._data, (priority, next(self._counter), item))

    def pop(self) -> T:
        """
        Remove and return the item with the highest priority (lowest number).

        :return: Item with the highest priority
        :rtype: Any
        :raises IndexError: If the priority queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty PriorityQueue")
        return heapq.heappop(self._data)[2]

    def peek(self) -> T:
        """
        Return the item with the highest priority without removing it.

        :return: Item with the highest priority
        :rtype: Any
        :raises IndexError: If the priority queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek from empty PriorityQueue")
        return self._data[0][2]

    def is_empty(self) -> bool:
        """
        Check whether the priority queue contains any items.

        :return: True if the queue is empty, False otherwise
        :rtype: bool
        """
        return not self._data

    def clear(self) -> None:
        """Remove all items from the priority queue."""
        self._data.clear()