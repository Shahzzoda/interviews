# Implement a priority queue (AKA heap)
# A priority queue is a data structure that maintains a maximum 
# of a set of elements. Instead of FIFO, it maintains the queue
# in terms of their priority in an array. You can only access the 
# max element. A priority queue has the following functions:
#   - top - get top element
#   - insert - inserts an element into heap
#   - pop - remove the top element
# a priority queue is implemented as a binary max heap tree. A 
# binary heap has the following properties:
#   1. all levels must be filled one at a time with last one full
#       from left to right. in other words, must be a complete tree.
#   2. the root will be the largest element in the tree. this must 
#       hold for all nodes and therefore recursive subtrees.
# 


# so we have a binary treenode
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# we have a heap 
# the heap 
class Heap():
    def __init__(self):
        self.heap = []
        self.size = 0
        self.top = None
        
    def makeheap(self, arr):
        for n in arr:
            self.insert(n)
        print(self.heap)

    def insert(self, num):
        self.heap.append(num)
        self.size += 1
        self.bubbleUp(self.size)
        self.top = self.heap[0]
    
    # swap the parent with the index as long as the index val is 
    # larger than parent val, and the index is not the root 
    def bubbleUp(self, i):
        i = i - 1
        parent =  i // 2
        while (parent >= 0 and i > 0):
            if (self.heap[i] > self.heap[parent]):
                self.swap(parent, i)
                # temp = self.heap[parent]
                # self.heap[parent] = self.heap[i]
                # self.heap[i] = temp
            i = parent
            parent = i // 2

    #  you switch the last element with the first elemenet and then bubledown 
    def pop(self):
        self.swap(0, self.size-1)
        # temp = self.heap[0]
        # self.heap[0] = self.heap[self.size-1]
        # self.heap[self.size-1] = temp
        self.size -= 1
        self.heap.pop()
        self.bubbleDown(0)
        print self.heap

    # find the two childs of the given index, swap the index with the largest 
    # child until both children are less than the given index or it has no 
    # childred
    def bubbleDown(self, i):
        left = i * 2 + 1 
        right = i * 2 + 2
        if i > self.size-1 or (left > self.size-1 and right > self.size-1):
            return
        if (left > self.size-1):
            if(self.heap[right] > self.heap[i]):
                self.swap(right, i)
                self.bubbleDown(right)
        elif (right > self.size-1):
            if(self.heap[left] > self.heap[i]):
                self.swap(left, i)
                self.bubbleDown(left)
        else:
            if(self.heap[left] > self.heap[right]):
                self.swap(left, i)
                self.bubbleDown(left)
            else:
                self.swap(right, i)
                self.bubbleDown(right)

    def swap(self, i, j):
        temp = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = temp

# heap = Heap()
# heap.makeheap([1, 2, 3, 4, 5, 6, 6, 9, 10])
# print "now we try popping"
# heap.pop()

t = [(1, 2), (2, 3), (9,||||