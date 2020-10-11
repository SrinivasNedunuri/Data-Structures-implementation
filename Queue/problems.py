import DCAQueue as LLQ
que = LLQ.Queue()
for i in range(5):
    que.enQueue(i)
print(que.que)
def reverseQueue(que):      #O(n)
    stack = []
    while not que.isEmpty():
        stack.append(que.deQueue())
    print(stack)
    while stack:
        que.enQueue(stack.pop())
    return que.que

print(reverseQueue(que))

