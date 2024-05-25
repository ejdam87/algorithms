from lib.graph import Network
from lib.vertex import Vertex
from queue import Queue
from math import inf
from copy import deepcopy

def sap(res: Network, s: Vertex, t: Vertex) -> list[Vertex]:
    """
    The shortest augmenting path
    """
    q = Queue()
    q.put(s)
    visited = set()
    preds = {}
    preds[s] = None

    while not q.empty():
        u = q.get()

        if u == t:
            break

        for v in res.successors(u):
            if v in visited:
                continue

            visited.add(v)
            preds[v] = u
            q.put(v)

    if t not in preds:
        return []

    path = []
    while (t != None):
        path.append(t)
        t = preds[t]

    return list(reversed(path))

def bottleneck(res: Network, path: list[Vertex]) -> float:
    b = inf

    for i in range( 1, len(path) ):
        u = path[i - 1]
        v = path[i]
        e = res.get_edge(u, v)
        b = min(b, e.weight)

    return b

def augment_path(net: Network, res: Network, path: list[Vertex]) -> None:
    
    b = bottleneck(res, path)

    for i in range( 1, len(path) ):
        u = path[i - 1]
        v = path[i]

        e = net.get_edge(u, v)
        if e is None:
            e = net.get_edge(v, u)
            e.flow -= b
        else:
            e.flow += b


def fix_residual(net: Network, res: Network) -> None:
    
    for edge in net.edges:
        if edge.flow == edge.weight:
            er = res.get_edge( edge.v1, edge.v2 )
            res.rem_edge(er)
        elif edge.flow == 0:
            er = res.get_edge( edge.v2, edge.v1 )
            res.rem_edge(er)
        else:
            er = res.get_edge( edge.v1, edge.v2 )
            er.weight = edge.weight - edge.flow
            er = res.get_edge( edge.v2, edge.v1 )
            if er is None:
                res.add_edge( deepcopy(edge.v2), deepcopy(edge.v1), 0 )
            er = res.get_edge( edge.v2, edge.v1 )
            er.weight = edge.flow


def ford_fulkerson(net: Network, s: Vertex, t: Vertex) -> Network:

    residual = deepcopy(net)
    path = sap(residual, s, t)

    while path != []:
        augment_path(net, residual, path)
        fix_residual(net, residual)
        path = sap(residual, s, t)

    return net


net = Network(3)

net.add_edge(net.vertices[0], net.vertices[1], 5)
net.add_edge(net.vertices[1], net.vertices[2], 3)

s = net.vertices[0]
t = net.vertices[2]

ford_fulkerson(net, s, t)
net.show()
