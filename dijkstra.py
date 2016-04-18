class Dijkstra:

    def __init__(self, input):
        self.input = input
        self.path = []


    def calculate(self):
        return [self.calculateFromOrigin(i) for i, v in enumerate(self.input)]


    def calculateFromOrigin(self, origin):
        distance = [-1 for i in range(len(self.input))]
        path = [-1 for i in range(len(self.input))] # vector to get the best path

        # Distance from origin to itself is always 0
        distance.pop(origin)
        distance.insert(origin, 0)
        priority = range(len(self.input))

        while True:
            if (len(priority) == 0): break
            frm = self.getSmallestPossibleVertex(distance, priority)
            priority.remove(frm)
            options = self.getOptionList(self.input[frm])
            for [position, weight] in options:
                dist = distance[frm] + weight
                if distance[position] == -1 or dist < distance[position]:
                    distance.pop(position)
                    distance.insert(position, dist)
                    path.pop(position)
                    path.insert(position, frm)

        self.path.insert(origin, path)
        return distance


    def getSmallestPossibleVertex(self, distances, priority):
        smallestKey = -1
        smallestValue = -1
        for i, item in enumerate(distances):
            if (smallestValue == -1 or (item >= 0 and item < smallestValue)) and i in priority:
                smallestValue = item
                smallestKey = i
        return smallestKey


    def getOptionList(self, vector):
        return [[i, weight] for i, weight in enumerate(vector) if weight > 0]


    def getPath(self):
        return self.path


    def getBestPath(self, frm, to):
        return [i for i in reversed(self._getBestPath(frm, to, [to]))]


    def _getBestPath(self, frm, to, path):
        path_ = self.path[frm]
        lastNode = path_[to]
        path.append(lastNode)
        if (lastNode == frm):
            return path
        else:
            return self._getBestPath(frm, lastNode, path)



#################
# EXAMPLE OF USE
#################

input = [[0,0,1,0,0,1,0,0],
        [1,0,0,0,0,0,0,0],
        [0,1,0,1,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,1,1],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,0,0]]

dj = Dijkstra(input)
result = dj.calculate()

# Print one vector per line
if result:
    for v in result: print v
