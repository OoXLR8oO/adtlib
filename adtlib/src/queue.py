from dataclasses import dataclass, field
from typing import Any, Iterator, List


@dataclass
class Queue:
    """
    First-in, first-out (FIFO) queue.

    :param _data: Internal storage for queue items
    :type _data: List[Any]
    """

    _data: List[Any] = field(default_factory=list, repr=False)
    

    def __len__(self) -> int:
        """
        Get the number of items in the queue.

        :return: Queue size
        :rtype: int
        """
        return len(self._data)

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate from front to back of the queue.

        :return: Iterator over queue items
        :rtype: Iterator[Any]
        """
        return iter(self._data)

    def __reversed__(self) -> Iterator[Any]:
        """
        Iterate from back to front of the queue.

        :return: Reverse iterator over queue items
        :rtype: Iterator[Any]
        """
        return reversed(self._data)

    def __repr__(self) -> str:
        """
        Represent the queue.

        :return: String representation
        :rtype: str
        """
        return f"Queue({self._data!r})"


    @property
    def data(self) -> List[Any]:
        """
        Get the internal queue list (read-only).

        :return: List of items in the queue
        :rtype: List[Any]
        """
        return self._data


    def enqueue(self, item: Any) -> None:
        """
        Add an item to the back of the queue.

        :param item: Item to enqueue
        """
        self._data.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item.

        :return: The earliest enqueued item
        :rtype: Any
        :raises IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty Queue")
        return self._data.pop(0)

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
        Check if the queue is empty.

        :return: True if empty, False otherwise
        :rtype: bool
        """
        return len(self._data) == 0