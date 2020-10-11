class binaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

def preOrderRecursive(root, result):
    if not root:
        return
    result.append(root.data)
    preOrderRecursive(root.left, result)
    preOrderRecursive(root.right, result)
    return result

def preOrderIterative(root, result):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inOrderRecursive(root, result):
    if not root:
        return
    inOrderRecursive(root.left, result)
    result.append(root.data)
    inOrderRecursive(root.right, result)

def inOrderIterative(root, result):
    if not root:
        return
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

def postOrderRecursive(root, result):
    if not root:
        return
    postOrderRecursive(root.left, result)
    postOrderRecursive(root.right, result)
    result.append(root.data)

def postOrderIterative(root, result):
    if not root:
        return
    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None

def levelOrder(root, result):
    if not root:
        return
    que = []
    que.append(root)
    while que:
        node = que.pop(0)
        result.append(node.data)
        if node.right:
            que.append(node.right)
        if node.left:
            que.append(node.left)







