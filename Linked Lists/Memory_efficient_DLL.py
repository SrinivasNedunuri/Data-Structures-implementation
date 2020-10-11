class Node:
    def __init__(self):
        self.data = None
        self.ptrdiff = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setptrdiff(self, prev, next):
        self.prtrdiff = prev ^ next

    def getptrdiff(self):
        return self.ptrdiff

