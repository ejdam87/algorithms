#!/usr/bin/env python3
import math
from typing import Any, Optional, TextIO


class Node:
    """Trida Node slouzi k reprezentaci uzlu ve strome.

    Atributy:
        key     klic daneho uzlu
        parent  reference na rodice uzlu (None, pokud neexistuje)
        left    reference na leveho potomka (None, pokud neexistuje)
        right   reference na praveho potomka (None, pokud neexistuje)
    """

    def __init__(self) -> None:
        self.key: Any = None
        self.parent: Optional[Node] = None
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None


class BinarySearchTree:
    """Trida BinarySearchTree slouzi k reprezentaci binarniho vyhledavaciho
    stromu.

    Atributy:
        root    reference na korenovy uzel typu Node
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None


def insert_rec(node: Optional[Node], key: Any) -> Node:

    if not node:
        new = Node()
        new.key = key
        return new

    if key < node.key:
        node.left = insert_rec(node.left, key)
        node.left.parent = node
    elif key > node.key:
        node.right = insert_rec(node.right, key)
        node.right.parent = node

    return node


def insert(tree: BinarySearchTree, key: Any) -> None:
    """Vlozi novy uzel s klicem 'key' do stromu 'tree'."""
    
    if tree.root is None:
        new = Node()
        new.key = key
        tree.root = new
        return

    tree.root = insert_rec(tree.root, key)


def search_rec(node: Optional[Node], key: Any) -> Optional[Node]:
    
    if not node:
        return None

    if key == node.key:
        return node

    if key < node.key:
        return search_rec(node.left, key)

    if key > node.key:
        return search_rec(node.right, key)


def search(tree: BinarySearchTree, key: Any) -> Optional[Node]:
    """Vyhleda uzel s klicem 'key' ve strome 'tree'. Vrati uzel s hledanym
    klicem. Pokud se klic 'key' ve strome nenachazi, vraci None.
    """
    return search_rec(tree.root, key)


def minimum(node: Node) -> Node:

    while node.left:
        node = node.left

    return node

def maximum(node: Node) -> Node:

    while node.right:
        node = node.right

    return node

def succesor(node: Node) -> Node:
    
    if node.right:
        return minimum(node.right)


    while node.parent and node == node.parent.right:

        node = node.parent

    return node.parent

def predeccessor(node: Node) -> Node:
    
    if node.left:
        return maximum(node.left)

    while node.parent and node == node.parent.left:

        node = node.parent

    return node.parent

def transplant(tree: BinarySearchTree, u: Node, v: Optional[Node]) -> None:
    
    if u == tree.root:
        tree.root = v

    else:

        if u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

    if v is not None:
        v.parent = u.parent


def delete(tree: BinarySearchTree, node: Node) -> None:
    """Smaze uzel 'node' ze stromu 'tree' a obnovi vlastnost vyhledavaciho
    stromu.
    """
    
    # --- no children
    if node.left is None and node.right is None:

        if node == node.parent.left:
            node.parent.left = None
        else:
            node.parent.right = None

        return

    # --- One child
    if not node.left:
        transplant(tree, node, node.right)
        return

    if not node.right:
        transplant(tree, node, node.left)
        return

    # --- two children

    if node.left is not None and node.right is not None:

        succ = minimum(node.right)

        if succ == node.right:
            transplant(tree, node, succ)
            succ.left = node.left
            succ.parent = node.parent

        else:

            succ_right = succ.right
            succ_parent = succ.parent

            succ.parent = node.parent
            succ.left = node.left
            succ.right = node.right

            node.left.parent = succ
            node.right.parent = succ

            succ_parent.left = succ_right

        if node == tree.root:
            tree.root = succ


def height_rec(node: Optional[Node]) -> int:
    
    if not node:
        return -1

    left = height_rec(node.left)
    right = height_rec(node.right)

    return max(left, right) + 1


def height(tree: BinarySearchTree) -> int:
    """Vraci vysku stromu 'tree'."""
    
    return height_rec(tree.root)


def is_correct_rec(node: Optional[Node], low: float, high: float) -> bool:

    if not node:
        return True

    if node.key > high or node.key < low:
        return False

    return is_correct_rec(node.left, low, node.key) and is_correct_rec(node.right, node.key, high)


def is_correct_bst(tree: BinarySearchTree) -> bool:
    """Overi, zdali je strom 'tree' korektni binarni vyhledavaci strom.
    Pokud ano, vraci True, jinak False.
    """
    
    return is_correct_rec(tree.root, -math.inf, math.inf)


# Dodatek k graphvizu:
# Graphviz je nastroj, ktery vam umozni vizualizaci datovych struktur,
# coz se hodi predevsim pro ladeni. Tento program generuje nekolik
# souboru neco.dot v mainu. Vygenerovane soubory nahrajte do online
# nastroje pro zobrazeni graphvizu:
# http://sandbox.kidstrythisathome.com/erdos/
# nebo http://www.webgraphviz.com/ - zvlada i vetsi grafy.
#
# Alternativne si muzete nainstalovat prekladac z jazyka dot do obrazku
# na svuj pocitac.
def make_graphviz(node: Optional[Node], dot_file: TextIO) -> None:
    if node is None:
        return

    dot_file.write('"{}" [label="{}"]\n'.format(id(node), node.key))

    for child, side in (node.left, 'L'), (node.right, 'R'):
        if child is not None:
            dot_file.write('"{}" -> "{}"\n'.format(id(node), id(child)))
            make_graphviz(child, dot_file)
        else:
            dot_file.write('{nil} [label="",color=white]\n{node} -> {nil}\n'
                           .format(node=id(node), nil=side + str(id(node))))


def make_graph(tree: BinarySearchTree, filename: str) -> None:
    try:
        with open(filename, 'w') as dot_file:
            dot_file.write("digraph Tree {\n")
            dot_file.write("node [color=lightblue2, style=filled];\n")
            if tree is not None and tree.root is not None:
                make_graphviz(tree.root, dot_file)
            dot_file.write("}\n")
        print("Vykresleny strom najdete v souboru", filename)
    except Exception:
        print("Ve vykreslovani nastala chyba")


def helper_test_insert(tree: BinarySearchTree) -> bool:
    insert(tree, 3)

    if tree.root is None or tree.root.key != 3:
        print("NOK - chybne vkladani do prazdneho stromu")
        return False

    insert(tree, 1)

    assert tree.root.left
    if tree.root.key != 3 or tree.root.left.key != 1:
        print("NOK - chybne vkladani do leveho podstromu")
        return False

    insert(tree, 5)

    assert tree.root.right
    if tree.root.key != 3 or tree.root.right.key != 5:
        print("NOK - chybne vkladani do praveho podstromu")
        return False

    insert(tree, 2)

    assert tree.root.left.right
    if tree.root.left.right.key != 2:
        print("NOK - chybne vkladani do leveho podstromu")
        return False

    insert(tree, 4)

    assert tree.root.right.left
    if tree.root.right.left.key != 4:
        print("NOK - chybne vkladani do praveho podstromu")
        return False

    print("OK")
    return True


def test_insert() -> None:
    print("Test 1. insert: ", end='')

    tree = BinarySearchTree()

    if not helper_test_insert(tree):
        make_graph(tree, "insert.dot")


def init_test_tree() -> BinarySearchTree:
    tree = BinarySearchTree()

    nodes = [Node() for _ in range(7)]
    for i in range(7):
        nodes[i].key = i

    tree.root = nodes[3]

    tree.root.left = nodes[1]
    nodes[1].parent = tree.root
    nodes[1].left = nodes[0]
    nodes[0].parent = nodes[1]
    nodes[1].right = nodes[2]
    nodes[2].parent = nodes[1]

    tree.root.right = nodes[5]
    nodes[5].parent = tree.root
    nodes[5].left = nodes[4]
    nodes[4].parent = nodes[5]
    nodes[5].right = nodes[6]
    nodes[6].parent = nodes[5]

    return tree


def helper_test_delete(tree: BinarySearchTree) -> bool:
    assert tree.root and tree.root.left and tree.root.left.left

    delete(tree, tree.root.left.left)

    if tree.root.left.key != 1 or tree.root.left.left is not None:
        print("NOK - chybne mazani listu")
        return False

    delete(tree, tree.root)

    if (tree.root is None or tree.root.key != 4 or tree.root.left.key != 1 or
            tree.root.left.left is not None):
        print("NOK - chybne mazani korenu")
        return False

    delete(tree, tree.root.left)

    if tree.root.left.key != 2:
        print("NOK - chybne mazani uzlu v levem podstrome")
        return False

    print("OK")
    return True


def test_delete() -> None:
    print("Test 2. delete: ", end='')
    tree = init_test_tree()

    if not helper_test_delete(tree):
        make_graph(tree, "delete.dot")


def helper_test_search(tree: BinarySearchTree) -> bool:
    node = search(tree, 3)

    if node is None or node.key != 3:
        print("NOK - chybne hledani korene s hodnotou 3")
        return False

    node = search(tree, 2)

    if node is None or node.key != 2:
        print("NOK - chybne hledani listu s hodnotou 2")
        return False

    node = search(tree, 7)

    if node is not None:
        print("NOK - hledani prvku, ktery se ve strome nevyskytuje")
        return False

    print("OK")
    return True


def test_search() -> None:
    print("Test 3. search: ", end='')
    tree = init_test_tree()

    if not helper_test_search(tree):
        make_graph(tree, "search.dot")


def helper_test_height(tree: BinarySearchTree) -> bool:
    tree_height = height(tree)

    if tree_height != 2:
        print("NOK - vyska 2 != vase vyska {}".format(tree_height))
        return False

    node = Node()
    node.key = 7
    assert (
        tree.root and tree.root.right and tree.root.left and
        tree.root.right.right
    )
    tree.root.right.right.right = node
    node.parent = tree.root.left.right

    tree_height = height(tree)

    if tree_height != 3:
        print("NOK - vyska 3 != vase vyska {}".format(tree_height))
        return False

    print("OK")
    return True


def test_height() -> None:
    print("Test 4. height: ", end='')
    tree = init_test_tree()

    if not helper_test_height(tree):
        make_graph(tree, "height.dot")


def helper_test_is_correct_bst(tree: BinarySearchTree) -> bool:
    if not is_correct_bst(tree):
        print("NOK - strom je korektni binarni vyhledavaci strom")
        return False

    assert tree.root and tree.root.left
    tree.root.key = 0
    tree.root.left.left = None

    if is_correct_bst(tree):
        print("NOK - strom neni korektni binarni vyhledavaci strom")
        return False

    assert tree.root.left.right and tree.root.right and tree.root.right.left
    tree.root.key = 3
    tree.root.left.right.key = 4
    tree.root.right.left.key = 2

    if is_correct_bst(tree):
        print("NOK - strom neni korektni binarni vyhledavaci strom")
        return False

    print("OK")
    return True


def test_is_correct_bst() -> None:
    print("Test 5. is_correct_bst: ", end='')
    tree = init_test_tree()

    if not helper_test_is_correct_bst(tree):
        make_graph(tree, "correct.dot")


if __name__ == '__main__':
    test_insert()
    test_delete()
    test_search()
    test_height()
    test_is_correct_bst()
