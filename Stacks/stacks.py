class stacks:             #Static array implementation
    def __init__(self, limit = 10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            return 'Stack Overflow'
        else:
            self.stk.append(item)
        print('Stack after Push', self.stk)

    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow')
            return 0
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            return 'Stack Underflow'
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)


stack = stacks(5)
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(1)
stack.push(6)
stack.push(8)
print(stack.pop())
print(stack.peek())
print(stack.size())
print(stack.isEmpty())