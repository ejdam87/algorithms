from typing import TypeVar

E = TypeVar("E")

class UnionFind:
    def __init__(self) -> None:
        self.parents: dict[E, E] = {}

    def make_set(self, e: E) -> None:
        self.parents[e] = e

    def union(self, u: E, v: E) -> None:
        p1 = self.find(u)
        p2 = self.find(v)
        self.naive_linking(p1, p2)

    def naive_linking(self, p1: E, p2: E) -> None:
        assert p1 != p2
        self.parents[p1] = p2

    def find(self, u: E) -> E:
        while (self.parents[u] != u):
            u = self.parents[u]

        return u

    def show(self) -> None:
        print("digraph G {")
        for u, v in self.parents.items():
            print(f"{u} -> {v}")
        print("}")


def showcase() -> None:
    uf = UnionFind()
    for i in range(10):
        uf.make_set(i)

    for i in range(2, 10, 2):
        uf.union(0, i)

    assert uf.find(2) == uf.find(8) == uf.find(6)

    uf.show()

if __name__ == "__main__":
    showcase()
