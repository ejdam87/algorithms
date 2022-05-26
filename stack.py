#!/usr/bin/env python3

from typing import Optional, Any


class Item:
    """Trida Item slouzi pro reprezentaci objektu v zasobniku.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        below   reference na predchazejici prvek v zasobniku
    """

    def __init__(self) -> None:
        self.value: Any = None
        self.below: Optional[Item] = None


class Stack:
    """Trida stack reprezentuje zasobnik.

    Atributy:
        top     reference na vrchni prvek v zasobniku
    """

    def __init__(self) -> None:
        self.top: Optional[Item] = None


def push(stack: Stack, value: Any) -> None:
    """Metoda push() vlozi na vrchol zasobniku (stack) novy prvek
    s hodnotou (value).
    """
    
    new = Item()
    new.value = value
    new.below = stack.top
    stack.top = new


def pop(stack: Stack) -> Optional[Any]:
    """Metoda pop() odebere vrchni prvek zasobniku. Vraci hodnotu
    (value) odebraneho prvku, pokud je zasobnik prazdny vraci None.
    """
    
    if is_empty(stack):
        return None

    popped = stack.top
    stack.top = popped.below
    return popped.value


def is_empty(stack: Stack) -> bool:
    """Metoda is_empty() vraci True v pripade prazdneho zasobniku,
    jinak False.
    """
    return stack.top is None


# Testy implementace
def test_push_empty() -> None:
    print("Test 1. Vkladani do prazdneho zasobniku: ", end="")

    stack = Stack()
    push(stack, 1)

    if stack.top is None:
        print("FAIL")
        return

    if stack.top.value == 1 and stack.top.below is None:
        print("OK")
    else:
        print("FAIL")


def test_push_nonempty() -> None:
    print("Test 2. Vkladani do neprazdneho zasobniku: ", end="")

    stack = Stack()
    item = Item()
    item.below = None
    item.value = 1
    stack.top = item

    push(stack, 2)

    if stack.top is None:
        print("FAIL")
        return
    if stack.top.value == 2 and stack.top.below == item:
        print("OK")
    else:
        print("FAIL")


def test_pop_empty() -> None:
    print("Test 3. Odebirani z prazdneho zasobniku: ", end="")

    stack = Stack()
    value = pop(stack)

    if value is not None or stack.top is not None:
        print("FAIL")
    else:
        print("OK")


def test_pop_nonempty() -> None:
    print("Test 4. Odebirani z neprazdneho zasobniku: ", end="")
    stack = Stack()
    item = Item()
    item.value = 1
    item.below = None
    stack.top = item

    value = pop(stack)

    if value != 1 or stack.top is not None:
        print("FAIL")
    else:
        print("OK")


def test_is_empty_empty() -> None:
    print("Test 5. is_empty na prazdnem zasobniku: ", end="")

    stack = Stack()

    if is_empty(stack):
        print("OK")
    else:
        print("FAIL")


def test_is_empty_nonempty() -> None:
    print("Test 6. is_empty na neprazdnem zasobniku: ", end="")

    stack = Stack()
    item = Item()
    item.below = None
    item.value = 1
    stack.top = item

    if is_empty(stack):
        print("FAIL")
    else:
        print("OK")


if __name__ == '__main__':
    test_push_empty()
    test_push_nonempty()
    test_pop_empty()
    test_pop_nonempty()
    test_is_empty_empty()
    test_is_empty_nonempty()