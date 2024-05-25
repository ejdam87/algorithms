import vertex as v

class Edge:
    def __init__( self, v1: v.Vertex, v2: v.Vertex ) -> None:
        self.v1 = v1
        self.v2 = v2

    def get_vertices( self ) -> tuple[ v.Vertex, v.Vertex ]:
        return self.v1, self.v2

    def is_weighted( self ) -> bool:
        return False

    def is_directed( self ) -> bool:
        return False


class DEdge( Edge ):
    def is_weighted( self ) -> bool:
        return False

    def is_directed( self ) -> bool:
        return True


class WUEdge( Edge ):
    def __init__( self, v1: v.Vertex, v2: v.Vertex, w: float ) -> None:
        super().__init__( v1, v2 )
        self.weight = w

    def is_weighted( self ) -> bool:
        return True

    def is_directed( self ) -> bool:
        return False

    def get_weight( self ) -> bool:
        return self.weight


class WDEdge( WUEdge ):
    def is_directed( self ) -> bool:
        return True
