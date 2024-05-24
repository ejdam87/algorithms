from typing import List

def queens_check(current: List[int], new: int) -> bool:
    
    row = len(current)
    col = new

    for prow, pcol in enumerate(current):
        if col == pcol:
            return False
        
        if abs(col - pcol) == abs(prow - row):
            return False
    
    return True


def queens_rec(current: List[int], n: int, res: List[List[int]]) -> None:
    
    if len(current) == n:
        res.append(current[:])
        return

    for col in range(n):

        if queens_check(current, col):
            queens_rec(current + [col], n, res)


def queens(n: int) -> List[List[int]]:
    
    res: List[List[int]] = []
    queens_rec([], n, res)
    return res
