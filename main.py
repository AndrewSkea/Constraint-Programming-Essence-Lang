import enum


class ConstraintType(enum.Enum):
    DISEQUALITY=0,
    ADJACENCY=1



class AC:

    def __init__(self, n, d):
        self.domains = {}
        for i in range(n):
            self.domains[i] = [j for j in range(d)]

        self.binary_constraints = {(x, y):[ConstraintType.ADJACENCY]
                                    for y in range(n) for x in range(n) if x!=y}

        keys = self.binary_constraints.keys()
        for l in range(0, len(keys), 2):
            self.binary_constraints[keys[l]].append(ConstraintType.DISEQUALITY)


        print(self.domains)
        print(self.binary_constraints)


    def revise(i, j):
        bin_cons = self.binary_constraints[(i,j)]
        for 



if __name__ == "__main__":
    ac = AC(8, 8)


        

    


