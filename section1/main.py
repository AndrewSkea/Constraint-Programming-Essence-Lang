class Arc:
    def __init__(self, dv1, dv2, constraints):
        self.dv1 = dv1
        self.dv2 = dv2
        self.constraints = constraints

    def __str__(self):
        return "arc({},{})".format(self.dv1, self.dv2)


class AC1:
    def __init__(self, n, dv):
        # Variable setup
        self.n = n
        self.log = ""
        self.dv = dv
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
                self.arcs.append(Arc(i + 1, j + 1, c))

    def revise(self, arc):
        self.log += "\nRevising {}".format(str(arc))
        changed = False
        for di in self.dv[arc.dv1]:
            supported = False

            for dj in self.dv[arc.dv2]:
                if (di, dj) in arc.constraints:
                    supported = True

            if not supported:
                self.dv[arc.dv1].remove(di)
                self.log += "\nRemoving value {} from D({})".format(di, arc.dv1)
                changed = True
        if len(self.dv[arc.dv1]) == 0:
            self.log += "\nNo solution exists!"
        return changed

    def ac1(self, output_no):
        repeat = True
        while repeat:
            repeat = False
            for arc in self.arcs:
                if self.revise(arc):
                    repeat = True

        self.log += "\nFinished:\n{}".format(self.dv)

        with open("./output_{}.txt".format(output_no), "w") as f:
                f.write(self.log)

if __name__ == "__main__":
    size = 6
    dvs = [
        {
            1: [1],
            2: [2],
            3: [j for j in range(1, size+ 1)],
            4: [j for j in range(1, size+ 1)],
            5: [j for j in range(1, size + 1)],
            6: [j for j in range(1, size + 1)]
        }, {
            1: [1],
            2: [4],
            3: [j for j in range(1, size+ 1)],
            4: [j for j in range(1, size+ 1)],
            5: [j for j in range(1, size + 1)],
            6: [j for j in range(1, size + 1)]
        }, {
            1: [2],
            2: [4],
            3: [6],
            4: [j for j in range(1, size+ 1)],
            5: [j for j in range(1, size + 1)],
            6: [j for j in range(1, size + 1)]
        }
    ]

    for i, dv in enumerate(dvs):
        ac = AC1(size, dv)
        ac.ac1(i)
