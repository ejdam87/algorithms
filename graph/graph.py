import edge   as e
import vertex as v

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
            v1, v2 = edge.get_verices()
            if v == v1:
                yield v2

    def add_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        new = e.DEdge( v1, v2 )
        self.edges.append( new )
        return new


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
