class DiffMatrix:
    def __init__(self):
        self.size = 0
        self.matrix = [[]]

    def __getitem__(self, indicies):
        indexA, indexB = indicies
        return self.matrix[indexA][indexB]

    def __setitem__(self, indicies, distance):
        indexA, indexB = indicies
        self.matrix[indexA][indexB] = distance

    def createFromCsv(self, path):
        with open(path, "r") as file:
            matrix = [[float(i) for i in line.split(",")[1:]] for line in file]
            self.matrix = matrix
            self.size = len(matrix)

    def getLeastDifference(self, itemA):
        differences = self.matrix[itemA]
        return differences.index(min(differences))
