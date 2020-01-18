# Leetcode # 108 
# Given a sorted array: [1, 2, 3, 4, 5, 6, 7]
# return a balanced BST:
#         4
#     2       6
#   1   3   5   7

# Thinking process:
# There's one thing that's already evident to me:
# the array is sorted -> we can do binary serach on it! and we
#                        probably need to for this question


# arr = [1, 2, 3, 4, 5, 6, 7]
# thinking about this example and binary search on paper:
# theres a pattern I noticed 
# Stack 0: 
# l: 0, r: 6, mid = 3 -> this is the head arr[3] => 4 
# lets look at the left of it 
# Stack 1:
# l: 0, r: 2, mid = 1 -> this is head.left arr[1] => 2 
# let's say our algo keeps going left...
# Stack 2:
# l: 0, r: 0, mid = 0 -> this is head.left.left  arr[0] => 1 and go up the stack
#                        [this seems recursive, if so this could be base case]
# let's say we go up the stack now, we'll have this. 
# Stack 1:
# l: 0, r: 2, mid was 1 -> like binary search, we could now chose r = mid + 1  
# let's go right this time to this:
# Stack 2:
# l: 2, r: 2, mid = 2 -> create node arr[2] => 3 and exit. in case you're not 
#                        seeing it, we  now have 4, 2, 1, and 3. it looks like this rn:
#                                     4
#                                 2       
#                               1   3     
# and now we will go up another stack and get back to this:
# Stack 1: 
# l: 0, r: 2 we visited self, left and right child so we can go up agian 
# Stack 0:
# l: 0, r: 6, and mid was 3 -> so now we call it on the right and do it all over again. 
# Stack 1: l: 4, r: 6, mid = 5 -> create node arr[5] => 6 
# Stack 2: l: 4, r:4, mid 4 -> create node arr[4] => 5
#                                     4
#                                 2      6 
#                               1   3  5   
# Stack 1: l: 4, r: 6, mid = 5
# Stack 2: l: 6, r: 6, mid = 6 => create arr[6] => 7
# Stack 1
# Stack 0: return 
#                                     4
#                                 2      6 
#                               1   3  5   7

# After that lengthy explaination, the code should be clear to you: 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createBST(nums, 0, len(nums)-1)
    
    def createBST(self, nums, l, r):
        if l > r: return None
        if l == r:
            return TreeNode(nums[l])
            
        mid = (l + r) // 2
        parent = TreeNode(nums[mid])
        parent.left = self.createBST(nums, l, mid - 1)
        parent.right = self.createBST(nums, mid + 1, r)
        return parent

# Here's an even cleaner algorithm:
# def sortedArrayToBST(self, num):
#     if not num: return None

#     mid = len(num) // 2
#     root = TreeNode(num[mid])
#     root.left = sortedArrayToBST(num[:mid])
#     root.right = sortedArrayToBST(num[mid+1:])

#     return root
