# Implement the «splay tree» data structure (an adaptively
# self-balancing binary search tree). Provide at least the following
# operations:
#
#  • ‹insert›  – add an element to the tree (if not yet present)
#  • ‹find›    – find a previously added element (return a ‹bool›)
#  • ‹erase›   – remove an element
#  • ‹to_list› – return the tree as a sorted list
#  • ‹filter›  – remove all elements failing a given predicate
#  • ‹root›    – obtain a reference to the root node
#
# Nodes should have (at least) attributes ‹left›, ‹right› and
# ‹value›. The class which represents the tree should be called
# ‹SplayTree›.

# You can find the required algorithms online (wikipedia comes to
# mind, but also check out ‹https://is.muni.cz/go/ssyj4d› for some
# intuition how the tree works).

# The main operation is ‘splaying’ the tree, which moves a
# particular node to the root, while rebalancing the tree. How
# balanced the tree actually is depends on the order of splay
# operations. The tree will have an «expected» logarithmic depth
# after a random sequence of lookups (splays). If the sequence is
# not random, the balance may suffer, but the most-frequently looked
# up items will be near the root. In this sense, the tree is
# self-optimizing.

# Note: it's easier to implement ‹erase› using splaying than by using
# the ‘normal’ BST delete operation:
#
#  1. splay the to-be-deleted node to the root, then
#  2. join its two subtrees L and R:
#     ◦ use splay again, this time on the largest item of the
#       left subtree L,
#     ◦ the new root of L clearly can't have a right child,
#     ◦ attach the subtree R in place of the missing child.

from __future__ import annotations
from typing import Optional, Callable, List, TypeVar, Generic, Protocol


class SupportsLessThan( Protocol ):
    def __lt__( self: T, other: T ) -> bool: ...

T = TypeVar( 'T', bound = SupportsLessThan )


class Node(Generic[T]):

    def __init__(self, value: T) -> None:

        self.value = value
        self.left: Optional["Node[T]"] = None
        self.right: Optional["Node[T]"] = None
        self.parent: Optional["Node[T]"] = None


class SplayTree(Generic[T]):

    def __init__(self) -> None:

        self.root_node: Optional[Node[T]] = None
        self.prev_added: Optional[Node[T]] = None

    def splay(self, node: Node[T]) -> None:

        while node != self.root_node:

            if node.parent == self.root_node:
                zig(self, node)
                continue

            assert node.parent
            assert node.parent.parent

            if (node == node.parent.left and node.parent == node.parent.parent.left) or \
                 (node == node.parent.right and node.parent == node.parent.parent.right):

                zig_zig(self, node)
                continue

            if (node == node.parent.right and node.parent == node.parent.parent.left) or \
                 (node == node.parent.left and node.parent == node.parent.parent.right):

                zig_zag(self, node)
                continue

            assert False

    def insert(self, value: T) -> None:

        if self.find(value):
            return

        new = Node(value)

        prev = None
        current = self.root_node

        while current:

            prev = current

            if value < current.value:
                current = current.left

            else:
                current = current.right

        new.parent = prev

        if prev is None:
            self.root_node = new

        elif new.value < prev.value:
            prev.left = new
        else:
            prev.right = new

        self.prev_added = new
        self.splay(new)


    def root(self) -> Optional[Node[T]]:
        return self.root_node

    def find(self, value: T) -> bool:

        node = self.get_node(self.root(), value)

        if node:
            self.splay(node)

        return True if node else False

    def erase(self, value: T) -> None:
        
        tbd = self.get_node(self.root_node, value)
        
        if not tbd:
            return None

        self.erase_node(tbd)

    def get_node(self, current: Optional[Node[T]], value: T) -> Optional[Node[T]]:

        if not current:
            return None

        if current.value == value:
            return current

        elif value < current.value:
            return self.get_node(current.left, value)

        else:
            return self.get_node(current.right, value)

#  2. join its two subtrees L and R:
#     ◦ use splay again, this time on the largest item of the
#       left subtree L,
#     ◦ the new root of L clearly can't have a right child,
#     ◦ attach the subtree R in place of the missing child.
    
    def maximum(self) -> Node[T]:

        current = self.root_node
        assert current

        while current.right:
            current = current.right

        return current

    def erase_node(self, node: Node[T]) -> None:
        
        self.splay(node)

        left: SplayTree[T] = SplayTree()
        left.root_node = node.left

        right: SplayTree[T] = SplayTree()
        right.root_node = node.right

        if left.root_node is None:
            self.root_node = node.right

            if node.right:
                node.right.parent = None

            return

        left.splay(left.maximum())

        left.root_node.right = right.root_node
        left.root_node.parent = None

        if right.root_node:
            right.root_node.parent = left.root_node

        self.root_node = left.root_node

    def filter(self, predicate: Callable[[T], bool]) -> None:
        
        to_delete: List[Node[T]] = []
        filter_rec(self.root_node, predicate, to_delete)

        for node in to_delete:
            self.erase_node(node)

    def to_list(self) -> List[T]:
        
        res: List[T] = []
        list_rec(self.root_node, res)
        return res


def filter_rec(current: Optional[Node[T]],
               predicate: Callable[[T], bool],
               to_delete: List[Node[T]]) -> None:

    if not current:
        return

    if not predicate(current.value):
        to_delete.append(current)

    filter_rec(current.left, predicate, to_delete)
    filter_rec(current.right, predicate, to_delete)


def list_rec(current: Optional[Node[T]], res: List[T]) -> None:

    if not current:
        return

    list_rec(current.left, res)
    res.append(current.value)
    list_rec(current.right, res)


def rotate_left(tree: SplayTree[T], node: Node[T]) -> None:

    assert node

    right_child = node.right

    if not right_child:
        return

    node.right = right_child.left

    if right_child.left:
        right_child.left.parent = node

    right_child.parent = node.parent

    if node == tree.root_node:
        tree.root_node = right_child

    if (node.parent and node != tree.root_node) and node == node.parent.left:
        node.parent.left = right_child

    elif (node.parent and node != tree.root_node) and node == node.parent.right:
        node.parent.right = right_child

    node.parent = right_child
    right_child.left = node


def rotate_right(tree: SplayTree[T], node: Node[T]) -> None:

    assert node

    left_child = node.left

    if not left_child:
        return

    node.left = left_child.right

    if left_child.right:
        left_child.right.parent = node

    left_child.parent = node.parent

    if node == tree.root_node:
        tree.root_node = left_child

    if (node.parent and node != tree.root_node) and node == node.parent.right:
        node.parent.right = left_child

    elif (node.parent and node != tree.root_node) and node == node.parent.left:
        node.parent.left = left_child

    node.parent = left_child
    left_child.right = node


def zig(tree: SplayTree[T], node: Node[T]) -> None:
    
    assert node.parent

    if node == node.parent.left:
        assert node.parent
        rotate_right(tree, node.parent)
    else:
        assert node.parent
        rotate_left(tree, node.parent)


def zig_zig(tree: SplayTree[T], node: Node[T]) -> None:

    assert node.parent

    if node == node.parent.left:
        assert node.parent
        assert node.parent.parent
        rotate_right(tree, node.parent.parent)
        rotate_right(tree, node.parent)
    else:
        assert node.parent
        assert node.parent.parent
        rotate_left(tree, node.parent.parent)
        rotate_left(tree, node.parent)


def zig_zag(tree: SplayTree[T], node: Node[T]) -> None:
    
    assert node.parent

    if node == node.parent.right:
        rotate_left(tree, node.parent)
        rotate_right(tree, node.parent)
    else:
        rotate_right(tree, node.parent)
        rotate_left(tree, node.parent)
