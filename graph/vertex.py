
class Vertex:
    def __init__( self, id: int ) -> None:
        self.id = _id
        self.desc = str( self.id )

    def add_desc( self, desc: str ) -> None:
        self.desc = desc

    def __repr__( self ) -> str:
        return self.desc
