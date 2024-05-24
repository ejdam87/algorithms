#!/usr/bin/env python3
import random
from typing import List, Callable


# Vasim ukolem v teto implementacni uloze je naprogramovat zakladni
# radici algoritmy. Formulace problemu neni vzdy stejna jako je ve
# sbirce, musite splnit zadani v komentari nad funkci.
#
# Povinne jsou pro vas radici algoritmy InsertSort, MergeSort, QuickSort
# a CountingSort. Zbyle algoritmy presto doporucujeme naimplementovat.


def swap(array: List[int], i: int, j: int) -> None:
    """Pomocna funkce swap pro vas, bere argumenty pole 'array', ve kterem
    prohodi prvky na pozicich indexu 'i' a 'j'.
    """
    array[i], array[j] = array[j], array[i]


# TODO: dopsat tuto funkci
def insert_sort(array: List[int]) -> None:
    """Razeni vkladanim. V kazdem pruchodu se nasledujici prvek posouva
    v poli 'array' tak dlouho, dokud nenarazi na mensi prvek, nebo na zacatek.
    Velikost vstupniho pole ziskate pomoci 'len(array)'.
    """
    # TODO
    
    for i in range(len(array)):

        x = array[i]
        j = i - 1

        while j >= 0 and array[j] > x:

            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = x


def partition(array: List[int], left: int, right: int) -> int:
    
    pivot = array[right]
    i = left - 1

    for j in range(left, right + 1):

        if array[j] <= pivot:

            i += 1
            swap(array, i, j)

    return i



def quick_sort_in_place(array: List[int], i: int, j: int) -> None:
    """Razeni rozdelovanim (QuickSort). Zadane pole 'array' v rozsahu
    indexu 'i' a 'j' rekurzivne seradte bez pouziti pomocneho pole.
    Jako pivot se voli posledni prvek zadaneho rozsahu.
    """
    
    if i < j:

        index = partition(array, i, j)
        quick_sort_in_place(array, i, index - 1)
        quick_sort_in_place(array, index + 1, j)


def merge(
    array: List[int], aux: List[int], left: int, mid: int, right: int
) -> None:
    """Slevani pro razeni spojovanim (MergeSort). Zadane pole 'array'
    obsahuje 2 usporadane posloupnosti v intervalech od 'left' po 'mid'
    a od 'mid'+1 po 'right'. K spojeni pouzijte pomocne pole 'aux'.
    Vysledek ulozte v poli 'array'.
    """
    
    aux = array[:]

    a = left
    b = mid + 1

    for i in range(left, right + 1):
        
        if a <= mid and (b > right or aux[a] < aux[b]):
            array[i] = aux[a]
            a += 1
        else:
            array[i] = aux[b]
            b += 1


# TODO: dopsat tuto funkci
def merge_sort(
    array: List[int], aux: List[int], left: int, right: int
) -> None:
    """Razeni spojovanim (MergeSort). Seradte zadane pole 'array'
    v intervalu od indexu 'left' po index 'right'.
    Pouzijte pomocnou funkci 'merge' a pomocne pole 'aux'. Vysledek
    ulozte v poli 'array'.
    """
    
    if left < right:

        mid = (left + right) // 2
        merge_sort(array, aux, left, mid)
        merge_sort(array, aux, mid + 1, right)
        merge(array, aux, left, mid, right)


def counting_sort(array: List[int], low: int, high: int) -> None:
    """Razeni pocitanim (CountingSort). Seradte zadane pole 'array'
    pricemz o poli vite, ze se v nem nachazeji pouze hodnoty v intervalu
    od 'low' po 'high' (vcetne okraju intervalu).
    Modifikujte primo zadane pole, stejne jako v ostatnich algoritmech.
    """
    
    counts = [0 for i in range(low, high + 1)]

    for num in array:
        counts[num - low] += 1

    j = 0
    for i, count in enumerate(counts):

        while count > 0:
            array[j] = i + low
            j += 1
            count -= 1


# Nasledujici radici algoritmy nejsou povinne, presto je doporucujeme
# naimplementovat jako cviceni. Nejsou to nejtezsi radici algoritmy,
# takze je mozna vhodne je v ramci treninku implementovat drive nez
# zbyle optimalni radici algoritmy.


# TODO: dopsat tuto funkci
def min_index(array: List[int], i: int, j: int) -> int:
    """Pomocna funkce pro razeni vyberem. Vrati index nejmensiho prvku
    v poli 'array' mezi 'i' a 'j'-1.
    """
    # TODO
    pass


# TODO: dopsat tuto funkci
def select_sort(array: List[int]) -> None:
    """Seradte pole 'array' pomoci razeni vyberem."""
    # TODO
    pass


# TODO: dopsat tuto funkci
def bucket_sort(array: List[int], max_element: int) -> None:
    """Prihradkove razeni. Seradte pole 'array', pricemz vite, ze pole
    obsahuje pouze nezaporne hodnoty mensi nebo rovny 'max_element'. Vstupni
    hodnoty nemusite upravovat do intervalu <0, 1), staci chytre vyuzit
    celociselne deleni hodnotou 'max_element + 1' pri vkladani do bucketu.
    """
    # TODO
    pass


# Dale nasleduji kody potrebne k testum, needitujte je.

ELEMENT_COUNT = 10
MAX_ELEMENT = 50


def new_random_array(size: int, max_element: int = MAX_ELEMENT) -> List[int]:
    """Slouzi pro generovani noveho pole delky size."""
    return [random.randint(1, max_element) for _ in range(size)]


def is_correct_result(in_array: List[int], out_array: List[int]) -> bool:
    return sorted(in_array) == out_array


def run_quick_sort(array: List[int]) -> None:
    quick_sort_in_place(array, 0, len(array) - 1)


def run_merge_sort(array: List[int]) -> None:
    aux = [0 for i in range(len(array))]
    merge_sort(array, aux, 0, len(array) - 1)


def test_sort(sort: Callable[[List[int]], None]) -> None:
    print("Test 1.: jednoprvkove pole [1]: ")
    array1 = [1]
    orig = array1[:]
    sort(array1)

    if is_correct_result(orig, array1):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1] a bylo serazeno,")
        print("po volani sortu je vystup: {}".format(array1[0]))

    print("Test 2.: dvouprvkove pole [1, 2]: ")
    array2 = [1, 2]
    orig = array2[:]
    sort(array2)

    if is_correct_result(orig, array2):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2] a bylo serazeno,")
        print("po volani sortu je vystup: {}".format(array2))

    print("Test 3.: dvouprvkove pole [2, 1]: ")
    array3 = [2, 1]
    orig = array3[:]
    sort(array3)

    if is_correct_result(orig, array3):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [2, 1],")
        print("po volani sortu je vystup: {}".format(array3))

    print("Test 4.: serazene pole 10 prvku [1..10]: ")
    array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    orig = array4[:]
    sort(array4)

    if is_correct_result(orig, array4):
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2..10],")
        print(" po volani sortu je vystup: {}".format(array4))

    print("Test 5.: neserazene pole: ")
    array5 = new_random_array(ELEMENT_COUNT)
    print("Puvodni pole: {}".format(array5))
    orig = array5[:]
    sort(array5)

    if is_correct_result(orig, array5):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: {}".format(array5))


def test_insert_sort() -> None:
    print("Testy na InsertSort:")
    test_sort(insert_sort)


def test_quick_sort() -> None:
    print("\nTesty na QuickSort:\n")
    test_sort(run_quick_sort)


def test_merge() -> None:
    print("\nTesty na Merge z MergeSortu:\n")
    aux = [0 for i in range(ELEMENT_COUNT)]

    print("Test 1.: Merge 2 jednoprvkovych stejnych poli [1] a [1]:")
    array1 = [1, 1]
    merge(array1, aux, 0, 0, 1)

    if array1[0] == 1 and array1[0] == 1:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 1],")
        print("po volani Merge je vystup: {}".format(array1))

    print("Test 2.: Merge 2 jednoprvkovych stejnych poli [1] a [2]:")
    array2 = [1, 2]
    merge(array2, aux, 0, 0, 1)

    if array2[0] == 1 and array2[1] == 2:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [1, 2],")
        print("po volani Merge je vystup: {}".format(array2))

    print("Test 3.: dvouprvkove pole [2, 1]: ")
    array3 = [2, 1]
    merge(array3, aux, 0, 0, 1)

    if array3[0] == 1 and array3[1] == 2:
        print("OK")
    else:
        print("NOK, puvodni pole bylo [2, 1], vysledek mel byt [1, 2],")
        print("po volani Merge je vystup: {}".format(array3))

    print("Test 4.: desetiprvkove pole [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]:")
    array4 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    orig = array4[:]
    merge(array4, aux, 0, 4, 9)

    if is_correct_result(orig, array4):
        print("OK")
    else:
        print("NOK, vysledek mel byt [1..10],")
        print("po volani Merge je vystup: {}".format(array4))

    print("Test 5.: desetiprvkove pole [1, 1, 2, 2, 3, 1, 1, 2, 3, 3]:")
    array5 = [1, 1, 2, 2, 3, 1, 1, 2, 3, 3]
    orig = array5[:]
    merge(array5, aux, 0, 4, 9)

    if is_correct_result(orig, array5):
        print("OK")
    else:
        print("NOK, vysledek mel byt [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],")
        print("po volani Merge je vystup: {}".format(array5))


def test_merge_sort() -> None:
    print("\nTesty na MergeSort:")
    test_sort(run_merge_sort)


def run_counting_sort(array: List[int]) -> None:
    counting_sort(array, 0, MAX_ELEMENT)


def test_counting_sort() -> None:
    print("\nTesty na CountingSort:")
    test_sort(run_counting_sort)

    print("Test 6.: neserazene pole malo hodnot:")
    array = new_random_array(ELEMENT_COUNT, ELEMENT_COUNT // 3)
    orig = array[:]
    print("Puvodni pole: " + str(array))
    counting_sort(array, 0, ELEMENT_COUNT // 3)

    if is_correct_result(orig, array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))

    print("Test 7.: neserazene pole malo hodnot posunute:")
    array = new_random_array(ELEMENT_COUNT, ELEMENT_COUNT // 3)
    for i in range(ELEMENT_COUNT):
        array[i] += 20

    orig = array[:]
    print("Puvodni pole: {}".format(array))
    counting_sort(array, 20, 20 + ELEMENT_COUNT // 3)

    if is_correct_result(orig, array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))


def test_select_sort() -> None:
    print("\nTesty na SelectSort:")
    test_sort(select_sort)


def run_bucket_sort(array: List[int]) -> None:
    bucket_sort(array, MAX_ELEMENT)


def test_bucket_sort() -> None:
    print("\nTesty na BucketSort:")
    test_sort(run_bucket_sort)

    print("Test 6.: neserazene pole malo hodnot:")
    array = new_random_array(ELEMENT_COUNT, ELEMENT_COUNT // 3)
    orig = array[:]
    print("Puvodni pole: {}".format(array))
    bucket_sort(array, ELEMENT_COUNT // 3)

    if is_correct_result(orig, array):
        print("OK")
    else:
        print("NOK: po volani sortu je vystup: " + str(array))


if __name__ == '__main__':
    test_insert_sort()
    test_quick_sort()
    test_merge()
    test_merge_sort()
    test_counting_sort()
    # BONUS
    test_select_sort()
    test_bucket_sort()
