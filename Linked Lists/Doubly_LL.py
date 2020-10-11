class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None

    def setPrev(self, prev):
        self.prev = prev

    def getPrev(self):
        return self.prev

    def hasPrev(self):
        return self.prev != None

    def __str__(self):
        return 'Node[Data = %s]'%(self.data,)

class d_linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = self.listlength()

    def listlength(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def show(self):
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()

    def getNode(self, index):
        current = self.head
        if current == None:
            return None
        if index >= self.length or index < 0:
            return None
        i = 0
        while i < index and current.getNext() is not None:
            current = current.getNext()
            if current == None:
                break
            i += 1
        return current

    def insertAtBeginining(self, data):
        newNode = Node(data, None, None)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node(data, None, None)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(data, None, current))
            self.tail = current.getNext()
            self.length += 1

    def insertAtPos(self, index, data):
        if index == 0:
            self.insertAtBeginining(data)
        elif index == self.length -1:
            self.insertAtEnd(data)
        else:
            newNode = Node(data, None, None)
            i = 0
            current = self.head
            previous = None
            while i < index:
                previous = current
                current = current.getNext()
                i += 1
            newNode.setNext(current)
            newNode.setPrev(previous)
            previous.setNext(newNode)
            current.setPrev(newNode)
            self.length += 1

    def delFirstNode(self):
        if self.head:
            node = self.head
            self.head = node.getNext()
            self.length -= 1
        else:
            print('list is empty')

    def delLastNode(self):
        lastNode = self.tail
        newlast = lastNode.getPrev()
        newlast.setNext(None)
        self.tail = newlast
        self.length -= 1

    def delAtPos(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Invalid index')
        elif index == 0:
            self.delFirstNode()
        elif index == self.length-1:
            self.delLastNode()
        else:
            currentNode = self.head
            previousNode = None
            i = 0
            while i < index:
                previousNode = currentNode
                currentNode = currentNode.getNext()
                i += 1
            previousNode.setNext(currentNode.getNext())
            currentNode.getNext().setPrev(previousNode)
            self.length -= 1
            
        #
