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
#       hold for all nodes / subtrees.
# Note: The passage above describes the Binary Max Heap, however, binary 
# min heaps are a thing! Istead of maintaining the max, it retains the 
# minimum element. 


# we have a Heap Object that represents the Binary Max Heap.
class Heap():
    def __init__(self):
        self.heap = []      # are heap will be set as an array. 
        self.size = 0       # size look up will be O(1) if we maintain it here
        self.top = None     # getting the max will be O(1) as well.
        
    # to build a heap from an array, you can just keep inserting with the helper fn
    def makeheap(self, arr):
        for n in arr:
            self.insert(n)
        print(self.heap)

    # this is essentially inserting at the end of the array, and letting
    # helper fn, bubbleUp, bring it up the tree to the right place. 
    def insert(self, num):
        self.heap.append(num)
        self.size += 1
        self.bubbleUp(self.size - 1) 
        self.top = self.heap[0]  # TODO: can we extract this into init?
    
    # swap the parent with the index as long as the index val is 
    # larger than parent val, and the index is not the root. 
    # the run time of this is O(logn) becuase it is a balanced binary tree
    # and we are always comparing the item to it's parents. instead of 
    # looking at every element (n) we are looking at logn bc a full binary
    # tree has height of logn
    def bubbleUp(self, i):
        parent =  i // 2
        while (parent >= 0 and i > 0):
            if (self.heap[i] > self.heap[parent]):
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
            parent = i // 2

    # to pop, you switch the max element, with the element at the end of the 
    # array, decrement the size, and bubbleDown the top element, to it's right 
    # place. remember: pop gives you the largest element! 
    # runtime is O(logn) bc popping is O(1) and bubble down is O(logn)
    def pop(self):
        top = self.heap[0]
        self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
        self.size -= 1  # TODO: can we manage this in init function?
        self.heap.pop() # self.heap is the array! you want to run pop so python internally
                        # can accurately behave when you do operations such as append, pop, 
                        # size, expand, and so on! 
        self.bubbleDown(0) 
        print self.heap

    # find the two children of the given index/node, swap it with the largest 
    # child until both children are less than the given index or it has no 
    # children. the following method assumes only valid indexes, i, will be given
    # the runtime of this is also logn because the work we do is proportional to 
    # the height, much like bubble up. bubble up looks at the parents, and bubble 
    # down looks at the children. this is a constant larger, but constants are dropped 
    # in big O analysis
    def bubbleDown(self, i):
        left = i * 2 + 1 
        right = i * 2 + 2
        
        # if both left and right is out of bounds, return. this is the base case
        # as it means it is all the way at the end.
        if left > self.size-1 and right > self.size-1: return

        # if the left index is out of bounds, and the right child is greater than i
        if (left > self.size-1 and self.heap[right] > self.heap[i]):
            self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
            self.bubbleDown(right) 
        # if the right index is out of bounds, and the left child is greater than i
        elif (right > self.size-1 and self.heap[left] > self.heap[i]):
            self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
            self.bubbleDown(left)
        else:
            # if both nodes are valid, compare them and swap i with the greater child
            if(self.heap[left] > self.heap[right]):
                self.heap[left], self.heap[i] = self.heap[i], self.heap[left]
                self.bubbleDown(left)
            else:
                self.heap[right], self.heap[i] = self.heap[i], self.heap[right]
                self.bubbleDown(right)


heap = Heap()
heap.makeheap([1, 2, 3, 4, 5, 6, 6, 9, 10])
print "now we try popping"
heap.pop()