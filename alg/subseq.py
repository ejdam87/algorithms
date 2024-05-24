
def maxprefix(seq: list[int], j: int, l: int) -> tuple[int, int]:
    
    s = 0
    i = j

    i_max = i
    s_max = -50000

    while i >= l:
        if s + seq[i] >= s_max:
            i_max = i
            s_max = s + seq[i]

        s = s + seq[i]
        i -= 1

    return s_max, i_max

def maxsuffix(seq: list[int], i: int, r: int) -> tuple[int, int]:
    
    s = 0
    j = i
    j_max = j
    s_max = -5000

    while j <= r:
        if s + seq[j] >= s_max:
            j_max = j
            s_max = s + seq[j]

        s = s + seq[j]
        j += 1

    return s_max, j_max


def maxsubseq(seq: list[int], i: int, j: int) -> tuple[int, int, int]:
    if i == j:
        return seq[i], i, j

    m = (i + j) // 2

    s1, i1, j1 = maxsubseq(seq, i, m)
    s2, i2, j2 = maxsubseq(seq, m + 1, j)

    assert s1 == sum(seq[i1: j1 + 1])
    assert s2 == sum(seq[i2: j2 + 1])

    s3a, i3 = maxprefix(seq, m, i)
    s3b, j3 = maxsuffix(seq, m, j)
    s3 = s3a + s3b - seq[m]
    assert s3 == sum(seq[i3: j3 + 1])

    return max( [ (s1, i1, j1), (s2, i2, j2), (s3, i3, j3) ], key=lambda x: x[0] )


def maxseq(seq: list[int]) -> tuple[int, int]:
    res = maxsubseq(seq, 0, len(seq) - 1)
    return res[1], res[2]

seq = [3, -5, 7, 0, -2, 6, 8, -9, 3]
i, j = maxseq(seq)
print( seq[i: j + 1] )
