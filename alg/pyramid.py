import nltk
from nltk.corpus import wordnet

## --- IsWord from assignment
## --- Assume O(|w|) running time
def is_word(w: str) -> bool:
    with open("eng.txt", "r") as f: ## TODO: Good english word list ?
        for line in f.readlines():
            if w == line.strip().lower():
                return True

    return False
## ---

## a)
## O(n * sqrt(n))
def longest_pyramid(seq: str) -> list[str]:
    
    n = len(seq)
    sought_length = 1
    res = []

    i = 0

    ## n iterations
    for j in range(n):
        assert i <= j

        ## we have a sequence of sought length in our buffer
        ## this branch is executed <= n-times
        if j - i + 1 == sought_length:

            ## O(|w|) to check if is a word + to create a string from seq
            ## best case: we find no word -> |w| is 1 for all iterations --> total complexity is in O(n)
            ## wors case: we find word at first try |w| is 1,2,3,...k; therefore n
            ##            is sum(1, 2,...k) = (k + 1) * (k / 2) = (k^2 + k) / 2; hence, k is in O(sqrt(n))
            ##            --> total complexity is in O(n * sqrt(n))
            if is_word( seq[i:(j+1)] ):

                ## in assignment, we would just increment our counter
                res.append( seq[i:(j+1)] )
                sought_length += 1
                i = j + 1

            ## we shift our buffer (j will be incremented by for loop)
            else:
                i += 1

    return res

seq = "TICAMYOUTENT".lower()

print(longest_pyramid(seq))

## b)
"""
We clearly cannot use our approach, since it is heavely dependent on the assumption that we know the length
of a word we seek. (That does not prove that we cannot use other greedy approach) TODO: Pockat na prednasku a zamysliet sa
"""

## c)
"""
With our greedy approach, it would not be possible, since our algorithm is strictly trying to maximize the number of words
in the pyramid. We can easily find a pyramid with lesser words but with more vowels in it. For example:
---
sequence: I MY AM OM YOU MYTH IDEA CRISP QUEUE GLYPHS
(of course without blank spaces (here we have it just as demonstration))

I MY MOM MYTH CRISP GLYPHS --> number of vowels = 3

vs.

I AM YOU IDEA QUEUE        --> number of vowels = 11
---
Therefore, our algorithm does not correctly solve the modified version of the problem.
"""

seq = "IMYAMOMYOUMYTHIDEACRISPQUEUEGLYPHS".lower()
print(longest_pyramid(seq))
