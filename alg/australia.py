import constraint as c

AUSTRALIA = {"WA"  : "Western Australia",
             "NT"  : "Northern Territory",
             "Q"   : "Queensland",
             "NSW" : "New South Wales",
             "V"   : "Victoria",
             "SA"  : "South Australia",
             "T"   : "Tasmania"}

short = list(AUSTRALIA)

NEIGHBOURS = [
             ("WA", "NT"),
             ("WA", "SA"),
             ("SA", "NT"),
             ("NT", "Q"),
             ("SA", "Q"),
             ("Q", "NSW"),
             ("SA", "NSW"),
             ("SA", "V"),
             ("NSW", "V")
             ]

COLORS = ["red", "green", "blue"]

problem = c.Problem()

for territory in short:
    problem.addVariable(territory, COLORS)

for s1, s2 in NEIGHBOURS:
    problem.addConstraint(lambda a, b: a != b, (s1, s2))
