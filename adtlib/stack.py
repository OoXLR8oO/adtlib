from dataclasses import dataclass, field
from typing import Iterator, List, Generic, TypeVar


T = TypeVar("T")

@dataclass
class Stack(Generic[T]):
    """
    Last-in, first-out (LIFO) stack.

    :param _data: Internal storage for stack items
    :type _data: List[Any]
    """
    _data: List[T] = field(default_factory=list, repr=False)

    def __len__(self) -> int:
        """
        Get the number of items in the stack.

        :return: Stack size
        :rtype: int
        """
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        """
        Iterate from bottom to top of the stack.

        :return: Iterator over stack items
        :rtype: Iterator[Any]
        """
        return iter(self._data)

    def __reversed__(self) -> Iterator[T]:
        """
        Iterate from top to bottom of the stack.

        :return: Reverse iterator over stack items
        :rtype: Iterator[Any]
        """
        return reversed(self._data)

    def __repr__(self) -> str:
        """
        Represent the stack.

        :return: String representation
        :rtype: str
        """
        return f"Stack({self._data!r})"

    @property
    def data(self) -> List[T]:
        """
        Get the internal stack list (read-only).

        :return: List of items in the stack
        :rtype: List[Any]
        """
        return self._data

    def push(self, item: T) -> None:
        """
        Add an item to the top of the stack.

        :param item: Item to push
        """
        self._data.append(item)

    def pop(self) -> T:
        """
        Remove and return the top item.

        :return: The last item added
        :rtype: Any
        :raises IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty Stack")
        return self._data.pop()

    def peek(self) -> T:
        """
        Return the top item without removing it.

        :return: The last item added
        :rtype: Any
        :raises IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek from empty Stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        :return: True if empty, False otherwise
        :rtype: bool
        """
        return len(self._data) == 0
