# Trees are often used to express some sort of hierarchy. Much like a
# graph and hashmap, it is not a linear data structure. It is noteworthy
# that trees are actually graphs with certain restrictions. There are
# different types of trees we can study but each tree has a root node, 
# each node has 0 or more child nodes. Each child node has one or more 
# child nodes. Every node, besides the root, has exactly one parent node
# Note: a tree is made up of subtrees.

# Tree vocabulary to talk about trees:
# - root: the node that has 0 parent nodes. start of the tree.
# - depth: the number of edges between node and the root.
# - height: the maximum number of edges in a tree (longest path size).
# - level: the number of edges between the a node and the root node.   

# Definitions for catagorizing trees:
# - binary: a tree where each node can have a maximum of two nodes. 
# - binary search tree: a binary tree where left child is less than the parent 
#       and the right child is equal to or greater than the parent node.   
# - balanced: a tree where the left and right subtree heights do not 
#       differ by more than 1. This is true for each node in the tree.
# - full (binary trees): where each node can have 0 or 2 nodes.
# - compelete: every level of the tree is full except the last one. 
#       the last level is full only from left to right.
# - tries: an n-ary tree that has characters for nodes. each path down a tree
#       may represent a word. 

# In interviews, you are often given the root tree node to deal with. For 
# tree problems you must know how to traverse a tree. There are three 
# ways of traversals: Preorder, Inorder, and Postorder.  

# For Binary trees
class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Building of the binary search tree
root = TreeNode(8)
n1= TreeNode(1)
n9= TreeNode(9)
n13= TreeNode(13)
n4= TreeNode(4)
n5= TreeNode(5)
root.left = n4
root.right = n13
n4.left = n1
n4.right = n5
n13.left = n9
#       8
#     /  \
#   4     13
#  / \   /
# 1   5 9


def inorder(node):
    if(node != None):
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if(node != None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if(node != None):
        preorder(node.left)
        preorder(node.right)
        print(node.data)

