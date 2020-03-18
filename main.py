class Constraint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def eval_constraint(self):
        return (𝑥𝑗 ≠ 𝑥𝑖) ∧ (𝑥𝑗 ≠ 𝑥𝑖 + (𝑗 − 𝑖)) ∧ (𝑥𝑗 ≠ 𝑥𝑖 − (𝑗 − 𝑖))



class AC1:
    def __init__(self, n, d):
        # Setup of the variables and their domains
        self.domains = {}
        for i in range(n):
            self.domains[i] = [j for j in range(d)]

        # Setup of constraint
        self.constraints =

    def revise(self, i, j):
        changed = False
        for di in self.domains[i]:
            supported = False

            print(self.domains)
            print(j)

            if any([True if di != dj else False for dj in self.domains[j] if
                    self.binary_constraints[(i, j)].count(ConstraintType.DISEQUALITY) > 0]):
                supported = True

            if not any([True if abs(di - dj) > 1 else False for dj in self.domains[j] if
                        self.binary_constraints[(i, j)].count(ConstraintType.ADJACENCY) > 0]):
                self.domains.pop(di)
                supported = True

            if not supported:
                self.domains.pop(di)

        if len(self.domains) == 0:
            return EnvironmentError("Failed to find solution")
        return changed






    def run_loop(self):
        repeat = True
        while repeat:
            repeat = False
            for arc in self.arcs:
                if self.revise(arc[0], arc[1]):
                    repeat = True


if __name__ == "__main__":
    ac = AC1(8, 8)
    ac.run_loop()
