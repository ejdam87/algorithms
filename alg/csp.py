from typing import Any, Callable

class Solver:

    def __init__( self ) -> None:

        self.variables: list[ str ] = []
        self.domains: dict[str, Any] = {}
        self.constraints: dict[ tuple[str], list[ Callable[ [ str ], bool ] ] ] = {}

        self.solutions: list[ dict[ str, Any] ] = []

    def add_variable( self,
                      name: str,
                      domain: list[Any] ) -> None:

        self.variables.append( name )
        self.domains[ name ] = domain

    def add_constraint( self,
                        constraint: Callable[ [ str ], bool ],
                        variables: tuple[ str ] ) -> None:

        if variables not in self.constraints:
            self.constraints[variables] = []

        self.constraints[variables].append( constraint )

    def solve( self ) -> list[ dict[ str, Any ] ]:
        self.solve_rec( 0, {} )
        return self.solutions


    def solve_rec( self, i: int, assignment: dict[ str, Any ] ) -> None:

        if i >= len( self.variables ):
            self.solutions.append( dict( assignment ) )
            return

        variable = self.variables[i]
        for value in self.domains[ variable ]:

            all_constraints_satisfied = True
            assignment[variable] = value

            for required, constraints in self.constraints.items():

                to_pass = []
                for var in required:
                    if var in assignment:
                        to_pass.append( assignment[ var ] )

                if len( to_pass ) == len( required ):
                    for constraint in constraints:
                        if  not constraint( *to_pass ):
                            all_constraints_satisfied = False

            if all_constraints_satisfied:
                self.solve_rec( i + 1, assignment )

            assignment.pop( variable )


solver = Solver()
solver.add_variable( "A", range(2, 5) )
solver.add_variable( "B", range(2, 4) )
solver.add_variable( "C", range(0, 7) )

solver.add_constraint( lambda a, b, c: a - b >= c, ("A", "B", "C") )
solver.add_constraint( lambda a, b, c: a * (b-1) != b + c, ("A", "B", "C") )
solver.add_constraint( lambda a, b: a != b, ("A", "B") )

print( solver.solve() )
