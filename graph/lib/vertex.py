
class Vertex:
    def __init__( self, _id: int ) -> None:
        self.id = _id
        self.desc = str( self.id )

    def add_desc( self, desc: str ) -> None:
        self.desc = desc

    def __hash__(self) -> int:
        return self.id

    def __eq__(self, oth) -> bool:
        if oth is None:
            return False

        return self.id == oth.id

    def __repr__( self ) -> str:
        return self.desc
