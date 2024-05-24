import math

MIN = 0
MAX = 1

class Node:
    def __init__(self, node_type: int, value: int | None = None) -> None:
        self.value = value
        self.node_type = node_type
        self.children: list["Node"] = []


class MinmaxTree:
    def __init__(self, root: Node | None = None) -> None:
        self.root = root


def minmax(tree: MinmaxTree) -> int | None:
    return minmax_rec(tree.root) if tree.root is not None else None

def minmax_rec(node: Node) -> int:
    
    if node.children == []:
        return node.value

    if node.node_type == MIN:
        res = math.inf
        for child in node.children:
            val = minmax_rec(child)
            res = min(val, res)
    else:
        res = -math.inf
        for child in node.children:
            val = minmax_rec(child)
            res = max(val, res)

    return res


def example_tree() -> MinmaxTree:
    
    res = MinmaxTree()
    root = Node(MAX)
    root.children = [Node(MIN), Node(MIN)]
    root.children[0].children = [Node(MAX), Node(MAX)]
    root.children[1].children = [Node(MAX), Node(MAX)]
    root.children[0].children[0].children = [Node(MIN, 7), Node(MIN, -5)]
    root.children[0].children[1].children = [Node(MIN, -math.inf), Node(MIN, 0)]
    root.children[1].children[0].children = [Node(MIN, 5)]
    root.children[1].children[1].children = [Node(MIN, math.inf)]
    res.root = root
    return res
