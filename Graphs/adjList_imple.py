class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.visited = False
        self.previous = None

    def addNeighbor(self, neighbor, weight = 0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getVertexID(self):
        return self.id

class Graph:
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDict.values())

    def addVertex(self, node):
        self.numVertices += 1
        newVertex = Vertex(node)
        self.vertDict[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if not frm in self.vertDict:
            self.addVertex(frm)
        if not to in self.vertDict:
            self.addVertex(to)
        self.vertDict[frm].addNeighbor(self.vertDict[to], cost)
        #for directed graph donot use this
        self.vertDict[to].addNeighbor(self.vertDict[frm], cost)

    def getVertices(self):
        return self.vertDict.keys()

    def setPrevious(self, current):
        self.previous = current

    def getEdges(self):
        edges = []
        for v in G:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid, wid, v.adjacent[w]))
        return edges



G = Graph()
G.addVertex('a')
G.addVertex('b')
G.addVertex('c')
G.addVertex('d')
G.addVertex('e')
G.addEdge('a', 'e', 10)
G.addEdge('a', 'c', 20)
G.addEdge('c', 'b', 30)
G.addEdge('b', 'e', 40)
G.addEdge('e', 'd', 50)
G.addEdge('f', 'e', 60)
print('Graph data:')
print(G.getEdges())

print(G.numVertices)


