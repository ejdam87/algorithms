
Interval = tuple[float, float]

def coverset( intervals: list[Interval] ) -> list[float]:
    """
    Find minimal set M of numbers s.t. each interval contains at least one number from M
    """

    sint = sorted(intervals, key=lambda x: x[0])
    res = []

    i = 0
    while i < len(sint):

        while i < len(sint) - 1 and sint[i + 1][0] <= sint[i][1]:
            i += 1

        res.append(sint[i][0])
        i += 1

    return res

intervals = [ (1, 6), (2, 7), (3, 5), (4, 8), (9, 10) ]
intervals = [ (3, 4), (5, 6), (7, 8) ]
intervals = [ (1, 10), (2, 9), (3, 8), (5, 6) ]

print(coverset(intervals))
