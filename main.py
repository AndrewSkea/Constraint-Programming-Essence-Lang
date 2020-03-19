class Arc:
    def __init__(self, dv1, dv2, constraints):
        self.dv1 = dv1
        self.dv2 = dv2
        self.constraints = constraints

    def __str__(self):
        return "arc({},{})".format(self.dv1, self.dv2)


class AC1:
    def __init__(self, n):
        # Variable setup
        self.n = n

        # Create the decision variables
        self.dv = {i: [j for j in range(1, self.n + 1)] for i in range(1, self.n + 1)}

        # Create the constraint network
        self.arcs = []
        for i in range(self.n):
            for j in range(self.n):
                if i == j: continue
                c = []
                for x in range(1, self.n + 1):
                    for y in range(1, self.n + 1):
                        if x != y and x != y + (i - j) and x != y - (i - j):
                            c.append((x, y))
                print(c)
                self.arcs.append(Arc(i + 1, j + 1, c))

    def revise(self, arc):
        changed = False
        for di in self.dv[arc.dv1]:
            supported = False

            for dj in self.dv[arc.dv2]:
                if (di, dj) not in arc.constraints:
                    supported = True

            if not supported:
                self.dv[arc.dv1].remove(di)
                print("Removing value {} from D({})".format(di, arc.dv1))
                changed = True
                print("Revising {}".format(str(arc)))
        if len(self.dv[arc.dv1]) == 0:
            raise Exception("No solution exists!")
        return changed

    def ac1(self):
        repeat = True
        while repeat:
            repeat = False
            for arc in self.arcs:
                if self.revise(arc):
                    repeat = True

        print("Finished:\n{}".format(self.dv))


if __name__ == "__main__":
    ac = AC1(6)
    ac.ac1()
