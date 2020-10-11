class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

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

class circular_LL:
    def __init__(self):
        self.head = None
        self.length = self.listlength()

    def listlength(self):                         #O(n) - Time complexity, O(1) - space complexity
        currentNode = self.head
        if currentNode == None:
            return 0
        count = 1
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            currentNode = currentNode.getNext()
            count += 1
        return count

    def show(self):                               #O(n) - Time complexity, O(1) - space complexity
        currentNode = self.head
        if currentNode == None:
            return'List is empty'
        print(currentNode.getData())
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            print(currentNode.getData())
            currentNode = currentNode.getNext()

    def insertAtEnd(self, data):                 #O(n) - Time complexity, O(1) - space complexity
        newNode = Node(data, None)
        newNode.setNext(newNode)
        currentNode = self.head
        if currentNode == None:
            self.head = newNode
        else:
            while currentNode.getNext() != self.head:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)
            newNode.setNext(self.head)
        self.length += 1

    def insertAtFront(self, data):                #O(n) - Time complexity, O(1) - space complexity
        newNode = Node(data, None)
        newNode.setNext(newNode)
        currentNode = self.head
        if currentNode == None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            while currentNode.getNext() != self.head:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)
            self.head = newNode
        self.length += 1

    def delAtEnd(self):                         #O(n) - Time complexity, O(1) - space complexity
        currentNode = self.head
        previousNode = None
        if currentNode == None:
            return 'List is empty'
        elif self.length == 1:
            self.head = None
            self.length -= 1
            return
        else:
            while currentNode.getNext() != self.head:
                previousNode = currentNode
                currentNode = currentNode.getNext()
            previousNode.setNext(self.head)
            self.length -= 1

    def delAtFront(self):                           #O(n) - Time complexity, O(1) - space complexity
        currentNode = self.head
        if currentNode == None:
            return 'List is empty'
        elif self.length == 1:
            self.head = None
            self.length -= 1
            return
        else:
            while currentNode.getNext() != self.head:
                currentNode = currentNode.getNext()
            currentNode.setNext(self.head.getNext())
            self.head = self.head.getNext()
            self.length -= 1
