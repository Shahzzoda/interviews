# Binary search can only be used on sorted arrays. Given an array, 
# it will repeatedly consider the approprirate halves of the array 
# and drill down to one index that matches or stop. It continually 
# the middle and pivots left or right of that. Here's a visual:
# array = [1 , 5, 14, 45, 99, 100, 115, 120] find: 99
#   l = 0  ^                       r = 7 ^    
#   note:  m = 3, arr[m] = 45 < 99, the val is after index m
# array = [1 , 5, 14, 45, 99, 100, 115, 120] find: 99
#                   l = 4 ^        r = 7 ^   
#   note:  m = 5, arr[m] = 100 > 99, the val is before index m
# array = [1 , 5, 14, 45, 99, 100, 115, 120] find: 99
#                l, r = 4 ^ 
#   note:  m = 4, arr[m] = 99 == 99, you found it! 


# Here's the iterative binary search algorithm:
def binarySearch1(nums, val):
    l, r = 0, len(nums) - 1
    while l <= r: 
        m = (l + r ) // 2
        if nums[m] > val:
            r = m - 1 
        elif nums[m] <  val:
            l = m + 1
        else:
            return m 
    else:
        return -1

# Here's the recursive binary search algorithm:
def binarySearch2(nums, val, l, r):
    if l > r: return -1
    m = (l + r) // 2 
    if nums[m] == val:return m 
    if nums[m] > val:
        return binarySearch2(nums, val, l, m-1)
    else:
        # meaning nums[m] <  val
        return binarySearch2(nums, val, m+1, r)
    
# Linear search is O(n)
# You go through every value in the array
# Binary search is O(log n)
# You go through the values diving n in half everytime, until we have 1 value.
# The number of steps you have is defined by how many times you have to divide 
# by two to get one -> this is the definition of Log(n) (with base 2, but we 
# drop the constant like that in Big-O analysis).