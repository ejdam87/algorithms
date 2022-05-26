#!/usr/bin/env python3

from contextlib import redirect_stdout
from io import StringIO
from typing import Any, List, Optional, TextIO, Callable, Tuple


class Node:
    """Trida Node slouzi k reprezentaci uzlu v B-strome.

    Atributy:
        keys        pole obsahujici klice daneho uzlu
        children    pole obsahujici reference na potomky
        leaf        urcuje, zdali je uzel list

    Poznamka: Narozdil od implementace z prednasky/sbirky zde nepouzivame pole
    pevne delky, ale Pythonovske seznamy, ktere muzeme zvetsovat pomoci
    seznam.append(prvek) a zmensovat pomoci seznam.pop().
    Z tohoto duvodu rovnez trida Node neobsahuje atribut n (pocet klicu),
    protoze pocet klicu muzeme snadno zjistit pomoci len(node.keys).
    """

    def __init__(self) -> None:
        self.keys: List[Any] = []
        self.children: List[Any] = []
        self.leaf: bool = False


class BTree:
    """Trida BTree slouzi k reprezentaci B-stromu

    Atributy:
        arity   pocet maximalnich potomku uzlu (stupen B-stromu je arity // 2)
        root    koren B-stromu
    """

    def __init__(self) -> None:
        self.arity: int = 0
        self.root: Optional[Node] = None


def inorder_rec(node: Optional[Node]) -> None:
    
    if not node:
        return

    for i in range(len(node.keys)):

        if not node.leaf:
            inorder_rec(node.children[i])

        print(node.keys[i])

    if not node.leaf:
        inorder_rec(node.children[-1])


def preorder_rec(node: Optional[Node]) -> None:

    if not node:
        return

    for key in node.keys:
        print(key)

    for child in node.children:
        preorder_rec(child)


def postorder_rec(node: Optional[Node]) -> None:

    if not node:
        return

    for child in node.children:
        postorder_rec(child)

    for key in node.keys:
        print(key)


def in_order_print(tree: BTree) -> None:
    """Vypise B-strom 'tree' pomoci inorder pruchodu. Pro vypis
    pouzivejte print. Hodnoty odsazujte mezerami nebo odradkovanim.
    """
    inorder_rec(tree.root)


def pre_order_print(tree: BTree) -> None:
    """Vypise B-strom 'tree' pomoci preorder pruchodu. Pro vypis
    pouzivejte print. Hodnoty odsazujte mezerami nebo odradkovanim.
    """
    preorder_rec(tree.root)


def post_order_print(tree: BTree) -> None:
    """Vypise B-strom 'tree' pomoci postorder pruchodu. Pro vypis
    pouzivejte print. Hodnoty odsazujte mezerami nebo odradkovanim.
    """
    postorder_rec(tree.root)


def search_rec(node: Optional[Node], key: Any) -> Optional[Node]:

    if not node:
        return None

    for i in range(len(node.keys)):

        if node.keys[i] == key:
            return node

        if key < node.keys[i]:

            index = i - 1 if i != 0 else i
            if not node.leaf:
                return search_rec(node.children[index], key)
            else:
                return None

    if node.leaf:
        return None
    else:
        return search_rec(node.children[-1], key)


def search(tree: BTree, key: Any) -> Optional[Node]:
    """Vyhleda uzel s klicem 'key' v B-strome 'tree'. Vrati uzel, ve
    kterem se nachazi klic. Pokud se klic 'key' v B-strome nenachazi,
    vraci None.
    """
    # TODO
    return search_rec(tree.root, key)



def preorder_traversal(node: Optional[Node], res: List[int]) -> None:

    if not node:
        return

    for key in node.keys:
        res.append(key)

    for child in node.children:
        preorder_traversal(child, res)


def is_equiv(tree1: BTree, tree2: BTree) -> bool:
    """Overi, jestli jsou 2 B-stromy ekvivalentni. Pokud ano, vraci
    True, jinak False.
    """
    
    preorder1 = []
    preorder2 = []

    preorder_traversal(tree1.root, preorder1)
    preorder_traversal(tree2.root, preorder2)

    return preorder1 == preorder2


def insert(tree: BTree, key: Any) -> None:
    """Vlozi klic 'key' do B-stromu 'tree'. Operace implementuje
    preemptivne stepeni. Muzete predpokladat, ze B-strom ma sudou aritu.
    """
    # TODO
    pass


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
def make_graphviz(
    node: Optional[Node], i: int, dot_file: TextIO, arity: int
) -> None:
    if node is None:
        return
    dot_file.write('node{} [label = "'.format(i))
    for key in enumerate(node.keys):
        dot_file.write("<f{}> |{}| ".format(key[0], key[1]))
    dot_file.write('<f{}>"];\n'.format(len(node.keys)))

    for child in enumerate(node.children):
        make_graphviz(child[1], (i + 1) * arity + child[0], dot_file, arity)

    if node.children:
        for j in range(len(node.children)):
            value = (i + 1) * arity + j
            dot_file.write('"node{}":f{} -> "node{}"\n'.format(i, j, value))


def make_graph(tree: BTree, filename: str) -> None:
    try:
        with open(filename, 'w') as dot_file:
            dot_file.write("digraph BTree {\n")
            dot_file.write("node [shape = record];\n")
            make_graphviz(tree.root, 0, dot_file, tree.arity)
            dot_file.write("}\n")
        print("Vykresleny B-strom najdete v souboru", filename)
    except Exception:
        print("Ve vykreslovani nastala chyba")


def create_node(keys: List[int], children: List[Node]) -> Node:
    node = Node()
    node.children = children
    node.keys = keys
    node.leaf = len(children) == 0
    return node


def test_tree_1() -> BTree:
    tree = BTree()
    tree.arity = 6

    node1 = create_node([1, 8, 12, 16, 25], [])

    tree.root = node1
    return tree


def test_tree_2() -> BTree:
    tree = BTree()
    tree.arity = 4

    node12 = create_node([55, 75], [])
    node11 = create_node([25], [])
    node10 = create_node([17], [])
    node9 = create_node([14, 15], [])
    node8 = create_node([9, 10, 12], [])
    node7 = create_node([6, 7], [])
    node6 = create_node([3], [])
    node5 = create_node([0, 1], [])
    node4 = create_node([16, 18, 50], [node9, node10, node11, node12])
    node3 = create_node([8], [node7, node8])
    node2 = create_node([2], [node5, node6])
    node1 = create_node([5, 13], [node2, node3, node4])

    tree.root = node1

    return tree


def test_tree_3() -> BTree:
    tree = BTree()
    tree.arity = 8

    node9 = create_node([66, 67, 68, 69, 70, 73, 79], [])
    node8 = create_node([40, 42, 47, 48, 50, 52, 56], [])
    node7 = create_node([36, 37, 38], [])
    node6 = create_node([29, 31, 32, 33, 34], [])
    node5 = create_node([23, 24, 27], [])
    node4 = create_node([18, 19, 20, 21], [])
    node3 = create_node([13, 15, 16], [])
    node2 = create_node([1, 3, 8], [])
    node1 = create_node([12, 17, 22, 28, 35, 39, 65],
                        [node2, node3, node4, node5,
                         node6, node7, node8, node9])

    tree.root = node1
    return tree


def test_tree_4() -> BTree:
    tree = BTree()
    tree.arity = 4

    node12 = create_node([55, 75], [])
    node11 = create_node([25], [])
    node10 = create_node([17], [])
    node9 = create_node([14, 15], [])
    node8 = create_node([9, 10, 12], [])
    node7 = create_node([5, 7], [])
    node6 = create_node([3], [])
    node5 = create_node([0, 1], [])
    node4 = create_node([16, 19, 50], [node9, node10, node11, node12])
    node3 = create_node([8], [node7, node8])
    node2 = create_node([2], [node5, node6])
    node1 = create_node([5, 13], [node2, node3, node4])

    tree.root = node1

    return tree


def capture(fun: Callable[[BTree], None], tree: BTree) -> List[int]:
    out = StringIO()
    with redirect_stdout(out):
        fun(tree)

    return list(map(int, out.getvalue().split()))


def test_in_order_print() -> None:
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 1. in_order_print: ")

    tree = helper_test_in_order_print()
    if tree is not None:
        make_graph(tree, "in_order.dot")


def helper_test_in_order_print() -> Optional[BTree]:
    res1 = [1, 8, 12, 16, 25]
    res2 = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18,
            25, 50, 55, 75]
    res3 = [1, 3, 8, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 27,
            28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 47, 48,
            50, 52, 56, 65, 66, 67, 68, 69, 70, 73, 79]

    tree = test_tree_1()
    res = capture(in_order_print, tree)

    if res1 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res1))
        return tree

    tree = test_tree_2()
    res = capture(in_order_print, tree)

    if res2 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res2))
        return tree

    tree = test_tree_3()
    res = capture(in_order_print, tree)

    if res3 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res3))
        return tree

    print("OK")
    return None


def test_pre_order_print() -> None:
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 2. pre_order_print: ")

    tree = helper_test_pre_order_print()
    if tree is not None:
        make_graph(tree, "pre_order.dot")


def helper_test_pre_order_print() -> Optional[BTree]:
    res1 = [1, 8, 12, 16, 25]
    res2 = [5, 13, 2, 0, 1, 3, 8, 6, 7, 9, 10, 12, 16, 18, 50, 14, 15,
            17, 25, 55, 75]
    res3 = [12, 17, 22, 28, 35, 39, 65, 1, 3, 8, 13, 15, 16, 18, 19, 20,
            21, 23, 24, 27, 29, 31, 32, 33, 34, 36, 37, 38, 40, 42, 47,
            48, 50, 52, 56, 66, 67, 68, 69, 70, 73, 79]

    tree = test_tree_1()
    res = capture(pre_order_print, tree)

    if res1 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res1))
        return tree

    tree = test_tree_2()
    res = capture(pre_order_print, tree)

    if res2 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res2))
        return tree

    tree = test_tree_3()
    res = capture(pre_order_print, tree)

    if res3 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res3))
        return tree

    print("OK")
    return None


def test_post_order_print() -> None:
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 3. post_order_print: ")

    tree = helper_test_post_order_print()
    if tree is not None:
        make_graph(tree, "post_order.dot")


def helper_test_post_order_print() -> Optional[BTree]:
    res1 = [1, 8, 12, 16, 25]
    res2 = [0, 1, 3, 2, 6, 7, 9, 10, 12, 8, 14, 15, 17, 25, 55, 75, 16,
            18, 50, 5, 13]
    res3 = [1, 3, 8, 13, 15, 16, 18, 19, 20, 21, 23, 24, 27, 29, 31, 32,
            33, 34, 36, 37, 38, 40, 42, 47, 48, 50, 52, 56, 66, 67, 68,
            69, 70, 73, 79, 12, 17, 22, 28, 35, 39, 65]

    tree = test_tree_1()
    res = capture(post_order_print, tree)

    if res1 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res1))
        return tree

    tree = test_tree_2()
    res = capture(post_order_print, tree)

    if res2 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res2))
        return tree

    tree = test_tree_3()
    res = capture(post_order_print, tree)

    if res3 != res:
        print("NOK")
        print("vysledek:\t   {}\nocekavany vysledek:{}".format(res, res3))
        return tree

    print("OK")
    return None


def test_search() -> None:
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 4. search: ")
    tree = helper_test_search()
    if tree is not None:
        make_graph(tree, "search.dot")


def helper_test_search() -> Optional[BTree]:
    tree = test_tree_1()

    node = search(tree, 16)
    if node is None or 16 not in node.keys:
        print("NOK - chybne hledani klice 16, ktery je v koreni B-stromu")
        return tree

    node = search(tree, 24)
    if node is not None:
        print("NOK - chybne hledani klice, ktery se v B-strome nenachazi")
        return tree

    tree = test_tree_2()

    node = search(tree, 15)
    if node is None or 15 not in node.keys:
        print("NOK - chybne hledani klice 15, ktery je v listu")
        return tree

    node = search(tree, 50)
    if node is None or 50 not in node.keys:
        print("NOK - chybne hledani klice 50, ktery je ve vnitrnim uzlu")
        return tree

    node = search(tree, 19)
    if node is not None:
        print("NOK - chybne hledani klice, ktery se v B-strome nenachazi")
        return tree

    print("OK")
    return None


def test_is_equiv() -> None:
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 5. is_equiv: ")

    trees = helper_test_is_equiv()
    if trees is not None:
        make_graph(trees[0], "t1.dot")
        make_graph(trees[1], "t2.dot")


def helper_test_is_equiv() -> Optional[Tuple[BTree, BTree]]:
    tree1 = test_tree_1()
    tree2 = test_tree_2()

    if is_equiv(tree1, tree2):
        print("NOK - B-stromy nejsou ekvivalentni, nemaji shodnou aritu")
        return tree1, tree2

    tree1 = test_tree_2()
    tree2 = test_tree_4()

    if is_equiv(tree1, tree2):
        print("NOK - B-stromy nejsou ekvivalentni, nemaji shodne hodnoty")
        return tree1, tree2

    tree1 = test_tree_2()
    tree2 = test_tree_2()

    if not is_equiv(tree1, tree2):
        print("NOK - B-stromy jsou ekvivalentni")
        return tree1, tree2

    print("OK")
    return None


def test_insert() -> None:
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
    print("Test 6. insert: ")

    tree = helper_test_insert()
    if tree is not None:
        make_graph(tree, "insert.dot")


def helper_test_insert() -> Optional[BTree]:
    tree = BTree()
    tree.arity = 4

    insert(tree, 1)

    if (tree.root is None) or (tree.root.keys != [1]):
        print("NOK - vkladani do prazdneho B-stromu stupne 2")
        return tree

    insert(tree, 7)
    insert(tree, 2)

    if (tree.root is None) or (tree.root.keys != [1, 2, 7]):
        print("NOK - vkladani do B-stromu bez stepeni")
        return tree

    insert(tree, 5)

    if (tree.root is None or
            tree.root.keys != [2] or
            tree.root.children[0].keys != [1] or
            tree.root.children[1].keys != [5, 7]):
        print("NOK - vkladani se stepenim korene")
        return tree

    insert(tree, 12)
    insert(tree, 8)

    if (tree.root is None or
            tree.root.keys != [2, 7] or
            tree.root.children[0].keys != [1] or
            tree.root.children[1].keys != [5] or
            tree.root.children[2].keys != [8, 12]):
        print("NOK - vkladani se stepenim listu")
        return tree

    insert(tree, 4)
    insert(tree, 3)
    insert(tree, 6)

    if (tree.root is None or
            tree.root.keys != [2, 4, 7] or
            tree.root.children[1].keys != [3] or
            tree.root.children[2].keys != [5, 6] or
            tree.root.children[3].keys != [8, 12]):
        print("NOK - vkladani se stepenim listu")
        return tree

    insert(tree, 11)

    if (tree.root is None or
            tree.root.keys != [4] or
            tree.root.children[0].keys != [2] or
            tree.root.children[1].keys != [7] or
            tree.root.children[1].children[0].keys != [5, 6] or
            tree.root.children[1].children[1].keys != [8, 11, 12]):
        print("NOK - vkladani se stepenim korene")
        return tree

    print("OK")
    return None


if __name__ == '__main__':
    test_in_order_print()
    test_pre_order_print()
    test_post_order_print()
    test_search()
    test_is_equiv()
    test_insert()
    print("# ## ## ## ## ## ## ## ## ## ## ## ## ## ")
