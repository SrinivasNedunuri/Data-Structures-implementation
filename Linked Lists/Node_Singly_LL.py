class Node:
    def __init__(self):
        self.data = None
        self.next = None

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

    def __str__(self):
        return 'node[%s]'%(self.data)

    def show(self):
        while self:
            print(self)
            self = self.next

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = self.listlength()

    def listlength(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def insertNodeAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    def insertNodeAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        current = self.head
        if self.length ==0:
            self.head = newNode
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
        self.length += 1

    def show(self):
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()

    def insertAtPos(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        elif pos == 0:
            self.insertNodeAtBeginning(data)
        elif pos == self.length:
            self.insertNodeAtEnd(data)
        else:
            newNode = Node()
            newNode.setData(data)
            count = 1
            current = self.head
            while count < pos:
                current = current.getNext()
                count += 1
            newNode.setNext(current.getNext())
            current.setNext(newNode)
            self.length += 1

    def deleteAtBeginnning(self):
        if self.head:
            self.head = self.head.getNext()
            self.length -= 1
        else:
            print('List is empty')

    def deleteAtEnd(self):
        if self.length == 0:
            print('List is empty')
        elif self.length == 1:
            self.head = None
            self.length -= 1
        else:
            current = self.head
            previous = self.head
            while current.getNext() != None:
                previous = current
                current = current.getNext()
            previous.setNext(None)
            self.length -= 1

    def deleteAtPos(self, pos):
        if self.length == 0:
            raise ValueError('list is empty')
        elif pos >= self.length:
            raise IndexError('No Node at specified position')
        elif pos == 0:
            self.deleteAtBeginnning()
        elif pos == self.length - 1:
            self.deleteAtEnd()
        else:
            current = self.head
            previous = self.head
            count = 0
            while count < pos:
                previous = current
                current = current.getNext()
                count += 1
            previous.setNext(current.getNext())
            self.length -= 1

    def deleteAtvalue(self, value):
        if self.length == 0:
            raise ValueError('list is empty')
        current = self.head
        previous = self.head
        while current.getData() != value or current.getNext != None:
            if current.getData() == value:
                previous.setNext(current.getNext())
                self.length -= 1
                return
            else:
                previous = current
                current = current.getNext()
        print('Value is not present')

    def clear(self):
        self.head = None
