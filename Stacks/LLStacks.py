class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None


class Stacks():
    def __init__(self, data = None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, item):
        temp = Node(item, None)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.head == None:
            raise IndexError
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        if self.head == None:
            raise IndexError
        return self.head.data

    def show(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

#our_list = ["first", "second", "third", "fourth"]
#our_stack = Stacks(our_list)
#print(our_stack.show())
#print(our_stack.pop())
#print(our_stack.pop())

