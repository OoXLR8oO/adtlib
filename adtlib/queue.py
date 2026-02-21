from dataclasses import dataclass, field
from typing import Any, Iterator, Iterable
from collections import deque


@dataclass
class Queue:
    """
    First-in, first-out (FIFO) queue.

    A simple queue ADT with methods to enqueue, dequeue, peek, and check if empty.

    :param _data: Internal storage for queue items
    :type _data: deque[Any]
    """
    _data: deque[Any] = field(default_factory=deque, repr=False)

    def __len__(self) -> int:
        """
        Return the number of items in the queue.

        :return: Number of items currently in the queue
        :rtype: int
        """
        return len(self._data)

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over items from front to back.

        :return: Iterator yielding items in enqueue order
        :rtype: Iterator[Any]
        """
        return iter(self._data)

    def __reversed__(self) -> Iterator[Any]:
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
    def data(self) -> Iterable[Any]:
        """
        Return a read-only view of the queue contents.

        :return: Iterable of items currently in the queue
        :rtype: Iterable[Any]
        """
        return self._data

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the back of the queue.

        :param item: Item to add to the queue
        :type item: Any
        """
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item from the queue.

        :return: The earliest enqueued item
        :rtype: Any
        :raises IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty Queue")
        return self._data.popleft()

    def peek(self) -> Any:
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