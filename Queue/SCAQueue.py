class Queue(object):
    def __init__(self, limit = 5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, item):
        if self.size >= self.limit:
            return 'Queue Overflow'
        else:
            self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print('Queue after EnQueue', self.que)

    def deQueue(self):
        if self.size <= 0:
            return 'Queue Underflow'
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print('Queue after deQueue', self.que)

    def queueRear(self):
        if self.rear is None:
            raise IndexError
        return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            raise IndexError
        return self.que[self.front]

    def size(self):
        return self.size


que =Queue()
que.enQueue("first")
print("Front: "+que.queueFront())
print ("Rear: "+que.queueRear())
que.enQueue("sccond")
print("Front: "+que.queueFront())
print("Rear: "+que.queueRear())
que.enQueue("third")
print("Front: "+que.queueFront())
print("Rear: "+que.queueRear())
que.deQueue()
print("Front: "+que.queueFront())
print("Rear: "+que.queueRear())
que.deQueue()
print("f'ront: "+que.queueFront())
print("Rear: "+que.queueRear())
#
