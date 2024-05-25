import lib.edge   as e
import lib.vertex as v

from typing import Iterator

class Graph:

    def __init__( self, size: int ) -> None:
        self.size = size
        self.vertices: list[ v.Vertex ] = [ v.Vertex( i ) for i in range(size) ]
        self.edges: list[ e.Edge ]      = []

    def get_verices( self ) -> list[ v.Vertex ]:
        return self.vertices

    def get_vertex_by_desc( self, desc: str ) -> v.Vertex:
        for vertex in self.vertices:
            if vertex.desc == desc:
                return vertex

        raise ValueError()

    def get_vertex_by_id( self, _id: int ) -> v.Vertex:
        return self.vertices[ _id ]

    def add_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        return NotImplemented

    def rem_edge(self, e: e.Edge) -> None:
        self.edges.remove(e)

    def successors( self, v: v.Vertex ) -> Iterator[ v.Vertex ]:
        return NotImplemented


class UGraph( Graph ):
    def successors( self, v: v.Vertex ) -> Iterator[ v.Vertex ]:
        """
        Un-weighted
        Un-directed
        """
        for edge in self.edges:
            v1, v2 = edge.get_verices()
            if v == v1:
                yield v2
            if v == v2:
                yield v1

    def add_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        new = e.Edge( v1, v2 )
        self.edges.append( new )
        return new


class DGraph( Graph ):
    def successors( self, v: v.Vertex ) -> Iterator[ v.Vertex ]:
        """
        Un-weighted
        Directed
        """
        for edge in self.edges:
            v1, v2 = edge.v1, edge.v2
            if v == v1:
                yield v2

    def add_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        new = e.DEdge( v1, v2 )
        self.edges.append( new )
        return new

    def get_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        for edge in self.edges:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge

        return None


class WUGraph( UGraph ):
    """
    Weighted
    Un-directed
    """
    def add_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        new = e.WUEdge( v1, v2 )
        self.edges.append( new )
        return new

class WDGraph( DGraph ):
    """
    Weighted
    Directed
    """
    def add_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        new = e.WDEdge( v1, v2 )
        self.edges.append( new )
        return new

class Network( WDGraph ):
    def add_edge( self, v1: v.Vertex, v2: v.Vertex, w: float ) -> e.Edge:
        new = e.NetworkEdge( v1, v2, w )
        self.edges.append( new )
        return new

    def show(self) -> None:
        print("Digraph N {")
        for i, vertex in enumerate(self.vertices):
            if i == self.size - 1:
                print(vertex)
            else:
                print(vertex, end=",")

        for edge in self.edges:
            print(f'{edge.v1} -> {edge.v2} [label="{edge.flow}/{edge.weight}"]')
        print()

        print("}")
