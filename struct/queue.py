#!/usr/bin/env python3

from typing import Optional, Any


class Item:
    """Trida Item slouzi pro reprezentaci objektu ve fronte.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        left    reference na dalsi prvek ve fronte
    """

    def __init__(self) -> None:
        self.value: Any = None
        self.left: Optional[Item] = None


class Queue:
    """Trida Queue reprezentuje frontu.

    Atributy:
        atribut first je reference na prvni prvek
        atribut last je reference na posledni prvek
    """

    def __init__(self) -> None:
        self.first: Optional[Item] = None
        self.last: Optional[Item] = None


def enqueue(queue: Queue, value: Any) -> None:
    """Metoda enqueue vlozi do fronty (queue) novy prvek s hodnotou
    (value).
    """
    
    new = Item()
    new.value = value

    if is_empty(queue):
        queue.first = new
        queue.last = new
        return

    queue.last.left = new
    queue.last = new
    return


def dequeue(queue: Queue) -> Optional[Any]:
    """Metoda dequeue odebere prvni prvek z fronty (queue).
    Vraci hodnotu (value) odebraneho prvku, pokud je fronta prazdna,
    vraci None
    """
    
    if is_empty(queue):
        return None

    res = queue.first
    queue.first = res.left

    if queue.first is None:
        queue.last = None

    return res.value


def is_empty(queue: Queue) -> bool:
    """is_empty() vraci True v pripade prazdne fronty, jinak False."""
    
    return queue.first is None


# Testy implementace
def test_enqueue_empty() -> None:
    print("Test 1. Vkladani do prazdne fronty: ", end="")

    queue = Queue()
    enqueue(queue, 1)

    if queue.first is None or queue.last is None:
        print("FAIL")
        return

    if (queue.first.value == 1 and queue.first.left is None and
            queue.last.value == 1 and queue.last.left is None):
        print("OK")
    else:
        print("FAIL")


def test_enqueue_nonempty() -> None:
    print("Test 2. Vkladani do neprazdne fronty: ", end="")

    queue = Queue()
    item = Item()
    item.left = None
    item.value = 1
    queue.first = item
    queue.last = item

    enqueue(queue, 2)

    if queue.first is None or queue.last is None:
        print("FAIL")
        return
    if (queue.last.value == 2 and queue.first == item and
            queue.first.left is not None and queue.first.left.value == 2):
        print("OK")
    else:
        print("FAIL")


def test_dequeue_empty() -> None:
    print("Test 3. Odebirani z prazdne fronty: ", end="")

    queue = Queue()
    value = dequeue(queue)

    if value is not None or queue.first is not None or queue.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_dequeue_nonempty() -> None:
    print("Test 4. Odebirani z neprazdne fronty: ", end="")

    queue = Queue()
    item = Item()
    item.value = 1
    item.left = None
    queue.first = item
    queue.last = item

    value = dequeue(queue)

    if value != 1 or queue.first is not None or queue.last is not None:
        print("FAIL")
    else:
        print("OK")


def test_is_empty_empty() -> None:
    print("Test 5. is_empty na prazdne fronte: ", end="")

    queue = Queue()

    if is_empty(queue):
        print("OK")
    else:
        print("FAIL")


def test_is_empty_nonempty() -> None:
    print("Test 6. is_empty na neprazdne fronte: ", end="")

    queue = Queue()
    item = Item()
    item.left = None
    item.value = 1
    queue.first = item
    queue.last = item

    if is_empty(queue):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_enqueue_empty()
    test_enqueue_nonempty()
    test_dequeue_empty()
    test_dequeue_nonempty()
    test_is_empty_empty()
    test_is_empty_nonempty()
