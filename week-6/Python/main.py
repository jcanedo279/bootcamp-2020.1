import math

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.leftNode, self.rightNode = None, None
    def setPrev(self, prevNode):
        self.prev = prevNode
    def setLeftNode(self, data):
        self.leftNode = Node(data)
    def setRightNode(self, data):
        self.rightNode = Node(data)
        

class Tree:
    def __init__(self):
        self.root = None
    def makeRoot(self, data):
        self.root = Node(data)
        self.root.setPrev('Root')
        
    ## Make current tree from an array
    def makeFromArr(self, arr):
        self.makeRoot(arr[0])
        for item in arr[1:]:
            self.binaryTreeInsert(item)
    def binaryTreeInsert(self, data):
        self.binaryTreeInsertNext(self.root, data)
    def binaryTreeInsertNext(self, curNode, data):
        if data < curNode.data:
            if curNode.leftNode == None:
                curNode.setLeftNode(data)
                curNode.leftNode.setPrev(curNode)
            else:
                self.binaryTreeInsertNext(curNode.leftNode, data)
        else:
            if curNode.rightNode == None:
                curNode.setRightNode(data)
                curNode.rightNode.setPrev(curNode)
            else:
                self.binaryTreeInsertNext(curNode.rightNode, data)
                
    def makeBalancedBST(self, arr):
        sortedArr = list(sorted(arr))
        midInd = math.floor(len(arr)/2)
        mid = sortedArr[midInd]
        left = arr[:mid]
        right = arr[mid+1:]
        self.makeRoot(mid)
        self.nextBST(self.root, left, right)
    def nextBST(self, curNode, left, right):
        if left:
            ## In case left is not empty
            midLeftInd = math.floor(len(left)/2)
            midLeft = left[midLeftInd]
            curNode.leftNode = Node(midLeft)
            self.nextBST(curNode.leftNode, left[:midLeftInd], left[midLeftInd+1:])
        if right:
            midRightInd = math.floor(len(right)/2)
            midRight = right[midRightInd]
            curNode.rightNode = Node(midRight)
            self.nextBST(curNode.rightNode, right[:midRightInd], right[midRightInd+1:])
            
    ## Print tree
    def printTree(self):
        print(f"tree =   {self.printNode(self.root)}")
    def printNode(self, curNode):
        s = f'{curNode.data} '
        if curNode.leftNode != None and curNode.rightNode == None:
            lS = self.printNode(curNode.leftNode)
            rS = 'xR'
            s += f'({lS} {rS})'
        elif curNode.leftNode == None and curNode.rightNode != None:
            lS = 'xL'
            rS = self.printNode(curNode.rightNode)
            s += f'({lS} {rS})'
        elif curNode.leftNode != None and curNode.rightNode != None:
            lS = self.printNode(curNode.leftNode)
            rS = self.printNode(curNode.rightNode)
            s += f'({lS} {rS})'
        return s
    
    def treeToArr(self):
        return self.treeToArrRec(self.root)
    def treeToArrRec(self, cur):
        arr = [cur]
        if cur.leftNode != None:
            leftSet = self.treeToArrRec(cur.leftNode)
            arr.extend(leftSet)
        if cur.rightNode != None:
            rightSet =  self.treeToArrRec(cur.rightNode)
            arr.extend(rightSet)
        return arr
        
        
        
        
## Q1
def diffRandNode(tree):
    print('-'*10 + 'Q1: maxDifference of rand node' + '-'*10)
    import random as rd
    arr = tree.treeToArr()
    randNode = arr[rd.randrange(0, len(arr))]
    print(randNode.data, maxDifference(randNode))  
## The maximum difference between a node and its descendents is the difference between it and the root node
def maxDifference(node):
    dist = 0
    cur = node
    while(cur.prev) != 'Root':
        dist += 1
        cur = cur.prev
    return dist

## Q2
def printLeafNodes(tree):
    print('-'*10 + 'Q2: print leaf nodes' + '-'*10)
    leafNodes = getLeaves(tree)
    for leafNode in leafNodes:
        print(nodePath(leafNode))
def getLeaves(tree):
    return getNodeLeaves(tree.root)
def getNodeLeaves(node):
    leaves = []
    if node.leftNode == None and node.rightNode == None:
        leaves.append(node)
    if node.leftNode != None:
        leaves.extend(getNodeLeaves(node.leftNode))
    if node.rightNode != None:
        leaves.extend(getNodeLeaves(node.rightNode))
    return leaves
def nodePath(node):
    path = []
    cur = node
    while(cur.prev != 'Root'):
        path.append(cur.data)
        cur = cur.prev
    return path

## Q3
def revTree(tree):
    print('-'*10 + 'Q3: reverse tree' + '-'*10)
    revTree = Tree()
    revTree.makeRoot(tree.root.data)
    revNodeRec(tree.root, revTree.root)
    return revTree
def revNodeRec(node, revNode):
    if node.leftNode != None:
        revNode.rightNode = Node(node.leftNode.data)
        revNodeRec(node.leftNode, revNode.rightNode)
    if node.rightNode != None:
        revNode.leftNode = Node(node.rightNode.data)
        revNodeRec(node.rightNode, revNode.leftNode)
    return revNode

def hw6(arr):
    print('-'*75)
    print(f'inputArr = {arr}\n')
    if not arr:
        print('the given array is empty, please re-try with another array')
        return
    myTree = Tree()
    myTree.makeFromArr(arr)
    myTree.printTree()
    ##Q1
    diffRandNode(myTree)
    ##Q2
    printLeafNodes(myTree)
    ##Q3
    revT = revTree(myTree)
    revT.printTree()
    print('-'*75 + '\n'*2)
    
        

arr0 = []
hw6(arr0)

arr = [0, 1, 2, 3 ,4, 5, 6, 7, 8]
hw6(arr)

arr2 = [4, 0, 1, 2, 3, 5, 6, 7, 8]
hw6(arr2)

myTree = Tree()
myTree.makeBalancedBST(range(10))
myTree.printTree()


