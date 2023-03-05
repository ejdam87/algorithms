from typing import List
from graph import Graph


WHITE = 1
GRAY  = 2
BLACK = 3

def dfs_limit(graph: Graph,
              current: int,
              limit: int,
              visited: List[int],
              order: List[int]) -> None:
    
    visited[current] = GRAY
    order.append(current)
    if limit == 0:
        return

    for succ in graph.succ[current]:
        if visited[succ] == WHITE:
            dfs_limit(graph, succ, limit - 1, visited, order)

    visited[current] = BLACK


def ids(graph: Graph) -> List[int]:

    order = []
    limit = 0

    visited = [WHITE for _ in range(graph.size)]

    while WHITE in visited:

        visited = [WHITE for _ in range(graph.size)]
        dfs_limit(graph, 0, limit, visited, order)
        limit += 1
    
    return order    # Order in which vertices were traversed
