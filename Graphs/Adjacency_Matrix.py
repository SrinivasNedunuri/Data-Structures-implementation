class vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False

    def setVertexId(self, id):
        self.id = id

    def getVertexId(self):
        return self.id

    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def getConnections(self, G):
        return G.adjMatrix[self.id]

    def setVisited(self):
        self.visited = True

    def __str__(self):
        return str(self.id)




class graph:
    def __init__(self, numOfVertices, cost = 0):
        self.adjMatrix = [[-1]*numOfVertices for _ in range(numOfVertices)]
        self.numVertices = numOfVertices
        self.vertices = []
        for i in range(0, numOfVertices):
            newVertex = vertex(i)
            self.vertices.append(newVertex)

    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexId(id)

    def getVertex(self, n):
        for vtxind in range(0, self.numVertices):
            print(self.vertices[vtxind].getVertexId())
            if n == self.vertices[vtxind].getVertexId():
                return vtxind
        return -1

    def addEdge(self, frm, to, cost = 0):
        if self.getVertex(frm) != -1 and self.getVertex(to) != -1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            #For directed graph do not add the below step unless there is a two way edge
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        vertices = []
        for vertind in range(0, self.numVertices):
            vertices.append(self.vertices[vertind].getVertexId())
        return vertices

    def printMatrix(self):
        for u in range(0, self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)

    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[v][u] != -1:
                    vid = self.vertices[v].getVertexId()
                    uid = self.vertices[u].getVertexId()
                    edges.append((vid, uid, self.adjMatrix[u][v]))
        return edges




G = graph(5)
G.setVertex(0, 'a')
G.setVertex(1, 'b')
G.setVertex(2, 'c')
G.setVertex(3, 'd')
G.setVertex(4, 'e')
print('Graph data:')
G.addEdge('a', 'e', 10)
G.addEdge('a', 'c', 20)
G.addEdge('c', 'b', 30)
G.addEdge('b', 'e', 40)
G.addEdge('e', 'd', 50)
G.addEdge('f', 'e', 60)

print(G.printMatrix())
print(G.getEdges())
print(G.getVertex('b'))
