class smartStack():
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, item):
        self.stack.append(item)
        if not self.min or item <= self.min[-1]:
            self.min.append(item)

    def pop(self):
        x = self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()
        return x

    def minimum(self):
        return self.min[-1]


stack = smartStack()
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(1)
stack.push(1)
stack.pop()
stack.pop()
print(stack.stack)
print(stack.min)

print(stack.minimum())