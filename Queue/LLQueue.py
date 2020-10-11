class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        self.last = None

    def setData(self, item):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setLast(self, last):
        self.last = last

    def getLast(self):
        return self.last

    def hasNext(self):
        return self.next != None

    def __str__(self):
        return '[Node = %s]'%(self.data)

class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, item):
        node = Node(item, self.front)
        self.last = self.front
        self.front = node
        if self.last:
            self.last.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
        self.size += 1

    def queueFront(self):
        if self.front is  None:
            raise IndexError
        return self.front

    def queueRear(self):
        if self.rear is None:
            raise IndexError
        return self.rear

    def deQueue(self):
        if self.rear is None:
            raise IndexError
        result = self.rear.getData()
        self.rear = self.rear.last
        self.size -= 1
        return result

    def size(self):
        return self.size

#que = Queue()
#que.enQueue("four")
#print("Front: ",que.queueFront())
#print ("Rear: ",que.queueRear())
#que.enQueue("five")
#print("Front: ",que.queueFront())
#print("Rear: ",que.queueRear())
#que.enQueue("six")
#print("Front: ",que.queueFront())
#print("Rear: ",que.queueRear())
#que.deQueue()
#print("Front: ",que.queueFront())
#print("Rear: ",que.queueRear())
#que.deQueue()
#print("f'ront: ",que.queueFront())
#print("Rear: ",que.queueRear())
#
