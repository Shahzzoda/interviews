# Linked Lists are a linear data structure where one node 
# points to another. A visual:
#  1 -> 2 -> 3 
# linked lists can also be doubly linked:
# 1 <-> 2 <-> 3 
# Since each node has two pointers, next and previous. Here is
# how we often are given or create on during interviews:

class Node(object):
    def __init__(self, val=None):
        self.val = val 
        self.next = None
        self.prev = None

    def __repr__(self):
        node = self
        while node != None:
            print node.val
            node = node.next
        return ""

class DoublyNode(Node):
    def __init__(self, val=None):
        Node.__init__(self, val)
        self.prev = None

class SinglyNode(Node):
    def __init__(self, val=None):
        Node.__init__(self, val)


# There are some common things you should know how to do in an interview, for each
# consider returning new, doing it in place, singly, doubly, and all edge cases:

# 1. Reverse a linked list
#   1 -> 2 -> 3 -> 4 -> None
def reversesingly1(head):
    if head == None or head.next == None: return head
    newhead = reversesingly1(head.next) # this will be the last element on the list 
    head.next.next = head
    head.next = None
    return newhead # we keep passing thew new head unchanged up the stack until returned

# I feel like I understand this and forget it way too many times so here's an 
# explaination:
# 1. if they gave you an empty linked list or you are on the last item, return head 
#    that last item (or empty head) will be the first node in your reversed linked list.
# 2. whatever is returned (like for instance, the first head) save it. and recursively call
#    the function passing on the next item (this will add stack calls all the way until 
#    we are at the last item)
# 3. now, this is the tricky part. this line gets called, after the stack calls have returned.  
#    for instance, for 1 -> 2 -> 3 -> 4 -> None, the first time this algo runs is on node 4
#    it has just returned and now you have newhead = 4, and head is 3, bc you are on that stack 
#    call. so head.next.next is setting 4's next to head which is 3. so you know have 
#    1 -> 2 -> 3 -> 4 -> None  to  1 -> 2 -> 3 -> None  4 -|
#              h   nh                        ^_____________|
#    and then you return 4 -> 3 -> None to the next stack call. In the next stack call, you 
#    have 3 as the head and 4 as the newhead. notice that you keep returning new head. this is the 
#    final head you'd want returned as the solution. so this time you have the following viz:
#    1 -> 2 -> 3 -> None         4 -> 3 -> None
#         h                      nh 
#    and now you make head's next (3) point to head (2) and and have head point to none like so:
#    1 -> 2 -> None  and  4 -> 3 -> 2 -> None
#    you get it. at the end, it returns with the reversed linked list. 

def reversesingly2(head):
    pass



# 2. Delete in a linked list in place and return the new head
def deleteNode(head, val):
    if head == None: return head
    if head.val == val: return head.next

    temp = head
    while head.next:
        if head.next.val == val:
            head.next = head.next.next
            break
        head = head.next
    return temp


# 3. Insert in a given position 
# 4. Merge two sorted linked list 

n1 = SinglyNode(1)
n2 = SinglyNode(2)
n3 = SinglyNode(3)
n4 = SinglyNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
print(deleteNode(n1, 1))
