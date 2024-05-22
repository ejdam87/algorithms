
Comparable_object = int ## for example

def divide(elements: list[Comparable_object], r: int) -> list[list[Comparable_object]]:
    groups = []
    i = 0
    while i < len(elements):
        group = []
        j = 0
        while j < r and i < len(elements):
            group.append(elements[i])
            j += 1
            i += 1

        groups.append(group)
    
    return groups

## passing only arrays of length 5 --> constant complexity
def median_of(l: list[Comparable_object]) -> Comparable_object:
    return sorted(l)[len(l) // 2]

def three_way_partition(l: list[Comparable_object], p: Comparable_object) -> tuple[ list[Comparable_object],
                                                                                    list[Comparable_object],
                                                                                    list[Comparable_object] ]:
    left = []
    middle = []
    right = []

    for e in l:
        if e < p:
            left.append(e)
        elif e == p:
            middle.append(e)
        else:
            right.append(e)

    return left, middle, right

def mom_select(elements: list[Comparable_object], k: int) -> int:
    
    ## if n >= 5 ---> C(n) <= O(11/5 * n) + C(n / 5) + C(7/10 * n)

    n = len(elements)

    # In lecture, here was 50 and merge_sort was used
    if n < 5:
        return sorted(elements)[k]

    r = 5 # size of one group
    groups = divide(elements, r) # O(n)

    # --- O(11/5 * n)
    medians = []
    for group in groups:    # n / 5 (+ 1) iterations
        if len(group) < r:
            continue
        
        medians.append(median_of(group)) # max r + 1 comparisons
    # ---

    ## median of medians recursively
    mom = mom_select(medians, n // r // 2)

    ## at least half of elements of <<medians>> is <= to mom --> (n/10)
    ## at least half of elements of <<medians>> is >= to mom --> (n/10)
    
    ## at least 3 elements from each 5-elem group (s.t. its median is <= to mom) is <= to mom --> 3 * (n/10)
    ## at least 3 elements from each 5-elem group (s.t. its median is >= to mom) is >= to mom --> 3 * (n/10)

    l, m, r = three_way_partition(elements, mom) # O(n)

    ## len(l) >= 3 * (n/10)
    ## len(r) >= 3 * (n/10)

    if k < len(l):
        return mom_select(l, k)
    elif k >= len(l) + len(m):
        return mom_select(r, k - len(l) - len(m))
    else:
        return mom

A = [5, 7, 14, 3, 15, 11, 10, 7, 8, 1, 21, 13]
print(sorted(A))
print(mom_select(A, 6))
