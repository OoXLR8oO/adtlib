from dataclasses import dataclass, field
from typing import Optional, Generator
from adtlib.node import TreeNode


@dataclass
class BinaryTree:
    """
    Binary tree data structure.

    :param root: Root node of the tree or None
    :type root: Optional[TreeNode]
    """
    _root: Optional[TreeNode] = field(default=None, repr=False)


    @property
    def root(self) -> Optional[TreeNode]:
        """
        Get the root node of the tree.

        :return: The root node or None
        :rtype: Optional[TreeNode]
        """
        return self._root

    @root.setter
    def root(self, node: Optional[TreeNode]) -> None:
        """
        Set the root node of the tree.

        :param node: Node to assign as root
        :type node: Optional[TreeNode]
        """
        self._root = node


    def is_empty(self) -> bool:
        """
        Determine whether the tree is empty.

        :return: True if the tree has no root node, otherwise False
        :rtype: bool
        """
        return self._root is None

    def clear(self) -> None:
        """
        Remove all nodes from the tree.
        """
        self._root = None

    def height(self, node: Optional[TreeNode] = None) -> int:
        """
        Compute the height of the tree or subtree.

        :param node: Node to compute height from, defaults to root
        :type node: Optional[TreeNode]
        :return: Height of the subtree, or -1 if empty
        :rtype: int
        """
        if node is None:
            node = self._root

        if node is None:
            return -1

        left_height = self.height(node.left) if node.left is not None else -1
        right_height = self.height(node.right) if node.right is not None else -1

        return 1 + max(left_height, right_height)

    def size(self) -> int:
        """
        Compute the total number of nodes in the tree.

        :return: Number of nodes
        :rtype: int
        """
        return sum(1 for _ in self.preorder())

    def preorder(self, node: Optional[TreeNode] = None) -> Generator[TreeNode, None, None]:
        """
        Traverse the tree in preorder.

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :yield: Nodes in preorder sequence
        :rtype: Generator[TreeNode, None, None]
        """
        if node is None:
            node = self._root

        if node is None:
            return

        yield node

        if node.left is not None:
            yield from self.preorder(node.left)

        if node.right is not None:
            yield from self.preorder(node.right)

    def inorder(self, node: Optional[TreeNode] = None) -> Generator[TreeNode, None, None]:
        """
        Traverse the tree in inorder.

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :yield: Nodes in inorder sequence
        :rtype: Generator[TreeNode, None, None]
        """
        if node is None:
            node = self._root

        if node is None:
            return

        if node.left is not None:
            yield from self.inorder(node.left)

        yield node

        if node.right is not None:
            yield from self.inorder(node.right)

    def postorder(self, node: Optional[TreeNode] = None) -> Generator[TreeNode, None, None]:
        """
        Traverse the tree in postorder.

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :yield: Nodes in postorder sequence
        :rtype: Generator[TreeNode, None, None]
        """
        if node is None:
            node = self._root

        if node is None:
            return

        if node.left is not None:
            yield from self.postorder(node.left)

        if node.right is not None:
            yield from self.postorder(node.right)

        yield node

    def level_order(self) -> Generator[TreeNode, None, None]:
        """
        Traverse the tree in level order.

        :yield: Nodes in level order sequence
        :rtype: Generator[TreeNode, None, None]
        """
        if not self._root:
            return

        queue = [self._root]

        while queue:
            node = queue.pop(0)
            yield node

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


@dataclass
class BinarySearchTree:
    """
    Binary Search Tree (BST) implementation.

    :param root: Root node of the BST, or None
    :type root: Optional[TreeNode]
    """
    _root: Optional[TreeNode] = field(default=None, repr=False)


    @property
    def root(self) -> Optional[TreeNode]:
        """
        Get the root node of the BST.

        :return: Root node or None
        :rtype: Optional[TreeNode]
        """
        return self._root

    @root.setter
    def root(self, node: Optional[TreeNode]) -> None:
        """
        Set the root node of the BST.

        :param node: Node to assign as root
        :type node: Optional[TreeNode]
        """
        self._root = node

    def is_empty(self) -> bool:
        """
        Check whether the BST is empty.

        :return: True if empty, else False
        :rtype: bool
        """
        return self._root is None

    def insert(self, value: int | float) -> None:
        """
        Insert a value into the BST.

        :param value: Value to insert
        :type value: int | float
        """
        def _insert(node: Optional[TreeNode], val: int | float) -> TreeNode:
            if node is None:
                return TreeNode(val)
            if val < node.value:
                node.left = _insert(node.left, val)
            elif val > node.value:
                node.right = _insert(node.right, val)
            # duplicate values are ignored
            return node

        self._root = _insert(self._root, value)

    def search(self, value: int | float) -> Optional[TreeNode]:
        """
        Search for a value in the BST.

        :param value: Value to find
        :type value: int | float
        :return: Node containing value, or None
        :rtype: Optional[TreeNode]
        """
        node = self._root
        while node:
            if value == node.value:
                return node
            node = node.left if value < node.value else node.right
        return None

    def inorder(self, node: Optional[TreeNode] = None) -> Generator[TreeNode, None, None]:
        """
        Inorder traversal (left → node → right).

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :yield: Nodes in ascending order
        :rtype: Generator[TreeNode, None, None]
        """
        node = node if node is not None else self._root
        if node:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)

    def preorder(self, node: Optional[TreeNode] = None) -> Generator[TreeNode, None, None]:
        """
        Preorder traversal (node → left → right).

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :yield: Nodes in preorder sequence
        :rtype: Generator[TreeNode, None, None]
        """
        node = node if node is not None else self._root
        if node:
            yield node
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)

    def postorder(self, node: Optional[TreeNode] = None) -> Generator[TreeNode, None, None]:
        """
        Postorder traversal (left → right → node).

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :yield: Nodes in postorder sequence
        :rtype: Generator[TreeNode, None, None]
        """
        node = node if node is not None else self._root
        if node:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node

    def min_node(self, node: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """
        Find the node with the minimum value.

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :return: Node with minimum value, or None
        :rtype: Optional[TreeNode]
        """
        node = node if node is not None else self._root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node

    def max_node(self, node: Optional[TreeNode] = None) -> Optional[TreeNode]:
        """
        Find the node with the maximum value.

        :param node: Starting node, defaults to root
        :type node: Optional[TreeNode]
        :return: Node with maximum value, or None
        :rtype: Optional[TreeNode]
        """
        node = node if node is not None else self._root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node