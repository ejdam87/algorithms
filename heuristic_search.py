from heapq import heappush, heappop
import graph as g
from typing import Callable, Any

Heuristic_type = Any

def greedy_best(g: g.WGraph,
                h: Heuristic_type,
                start: str,
                end: str) -> None:

    heap = [(h(start), start)]

    while heap:

        promise, node = heappop(heap)
        if node == end:
            return True

        for succ in g.neigbours(node):
            g.came_from[succ] = node
            heappush( heap, (h(succ), succ) )

    return False


def a_star(g: g.WGraph,
           h: Heuristic_type,
           start: str,
           end: str) -> bool:
    
    cost_so_far = {}
    cost_so_far[start] = 0
    heap = [(h(start), start)]

    while heap:

        promise, node = heappop(heap)
        if node == end:
            return True

        for succ in g.neigbours(node):

            next_cost = cost_so_far[node] + g[node][1]
            if succ not in cost_so_far or next_cost < cost_so_far[succ]:

                heappush( heap, (h(succ) + new_cost) )
                g.came_from[succ] = node

    return False


def example_map() -> g.WGraph:

    romania_map = g.WGraph(20)
    romania_map.add_node_description(['Arad', 'Bucharest', 'Craiova',
                                      'Drobeta', 'Eforie', 'Fagaras',
                                      'Giurgiu', 'Hirsova', 'Iasi',
                                      'Lugoj', 'Mehadia', 'Neamt',
                                      'Oradea', 'Pitesti', 'Rimnicu',
                                      'Sibiu', 'Timisoara', 'Urziceni',
                                      'Vaslui', 'Zerind'])

    romania_map.add_edge('Arad', 'Zerind', cost=75)
    romania_map.add_edge('Zerind', 'Arad', cost=75)

    romania_map.add_edge('Arad','Sibiu', cost=140)
    romania_map.add_edge('Sibiu', 'Arad', cost=140)

    romania_map.add_edge('Arad','Timisoara',cost=118)
    romania_map.add_edge('Timisoara', 'Arad',cost=118)

    romania_map.add_edge('Bucharest','Urziceni',cost=85)
    romania_map.add_edge('Urziceni', 'Bucharest',cost=85)

    romania_map.add_edge('Bucharest','Pitesti',cost=101)
    romania_map.add_edge('Pitesti', 'Bucharest',cost=101)

    romania_map.add_edge('Bucharest','Giurgiu',cost=90)
    romania_map.add_edge('Giurgiu','Bucharest',cost=90)

    romania_map.add_edge('Bucharest','Fagaras',cost=211)
    romania_map.add_edge('Fagaras','Bucharest',cost=211)

    romania_map.add_edge('Craiova','Drobeta',cost=120)
    romania_map.add_edge('Drobeta','Craiova',cost=120)

    romania_map.add_edge('Craiova','Rimnicu',cost=146)
    romania_map.add_edge('Rimnicu','Craiova',cost=146)

    romania_map.add_edge('Craiova','Pitesti',cost=138)
    romania_map.add_edge('Pitesti','Craiova',cost=138)

    romania_map.add_edge('Drobeta','Mehadia',cost=75)
    romania_map.add_edge('Mehadia','Drobeta',cost=75)

    romania_map.add_edge('Eforie','Hirsova',cost=86)
    romania_map.add_edge('Hirsova','Eforie',cost=86)

    romania_map.add_edge('Fagaras','Sibiu',cost=99)
    romania_map.add_edge('Sibiu','Fagaras',cost=99)

    romania_map.add_edge('Hirsova','Urziceni',cost=98)
    romania_map.add_edge('Urziceni','Hirsova',cost=98)

    romania_map.add_edge('Iasi','Vaslui',cost=92)
    romania_map.add_edge('Vaslui','Iasi',cost=92)

    romania_map.add_edge('Iasi','Neamt',cost=87)
    romania_map.add_edge('Neamt','Iasi',cost=87)

    romania_map.add_edge('Lugoj','Timisoara',cost=111)
    romania_map.add_edge('Timisoara','Lugoj',cost=111)

    romania_map.add_edge('Lugoj','Mehadia',cost=70)
    romania_map.add_edge('Mehadia','Lugoj',cost=70)

    romania_map.add_edge('Oradea','Zerind',cost=71)
    romania_map.add_edge('Zerind','Oradea',cost=71)

    romania_map.add_edge('Oradea','Sibiu',cost=151)
    romania_map.add_edge('Sibiu','Oradea',cost=151)

    romania_map.add_edge('Pitesti','Rimnicu',cost=97)
    romania_map.add_edge('Rimnicu','Pitesti',cost=97)

    romania_map.add_edge('Rimnicu','Sibiu',cost=80)
    romania_map.add_edge('Sibiu','Rimnicu',cost=80)

    romania_map.add_edge('Urziceni','Vaslui',cost=142)
    romania_map.add_edge('Vaslui','Urziceni',cost=142)

    return romania_map
