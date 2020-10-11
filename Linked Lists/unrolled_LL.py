class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedBlock:
    def __init__(self):
        self.head = None
        self.next = None
        self.nodeCount = 0

blockSize = 2
blockHead = None
def newLinkedBlock():
    block = LinkedBlock()
    block.head = None
    block.next = None
    block.nodeCount = 0
    return block
def newNode(data):
    temp = Node(data, None)
    temp.data = data
    return temp

def searchElements(blockHead, k):                      #O(sqrt(n))
    #find the block
        j = (k + blockSize - 1)//blockSize   #kth node is in jth block
        p = blockHead
        j -= 1
        while j:
            p = p.next
            j -= 1
        fLinkedBlock = p
    #find teh node
        q = p.head
        k = k % blockSize
        if k == 0:
            k = blockSize
        k = p.nodeCount + 1 - k
        k -= 1
        while k:
            q = q.next
            k -= 1
        fnode = q
        return fLinkedBlock, fnode

def shift(A):
    B = A
    global blockHead
    while(A.nodeCount > blockSize):
        if (A.next == None):
            A.next = newLinkedBlock()
            B = A.next
            temp = A.head.next
            A.head.next = A.head.next.next
            B.head = temp