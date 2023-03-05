import graph as g

def draw_directed(g: g.DGraph, file: str) -> None:

    with open(f"{file}.dot", "w") as f:
        f.write("digraph MyGraph {\n")

        for i, succ in enumerate(g.succ):
            for j in succ:
                f.write(f"{g.desc[i]} -> {g.desc[j]}\n")

        f.write("}\n")


def draw_weighted(g: g.WUGraph, file: str) -> None:

    with open(f"{file}.dot", "w") as f:
        f.write("digraph MyGraph {\n")

        for i, succ in enumerate(g.succ):
            for j, w in succ:
                f.write(f'{g.desc[i]} -> {g.desc[j]} [label="{w}"]\n')

        f.write("}\n")

def draw_graph(g: g.Graph, file: str) -> None:

    if type(g) == DiGraph:
        draw_directed(g, file)
    elif type(g) == WGraph:
        draw_weighted(g, file)
    else:
        assert False
