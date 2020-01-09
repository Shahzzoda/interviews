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
    start, end = 0, len(nums) - 1
    while start <= end: 
        mid = (start + end ) // 2
        if nums[mid] > val:
            end = mid - 1 
        elif nums[mid] <  val:
            start = mid + 1
        else:
            return mid 
    else:
        return -1

# Here's the recursive binary search algorithm:
def binarySearch2(nums, val, start, end):
    if start > end:
        return -1
        
    mid = (start + end) // 2 
    if nums[mid] == val:
        return mid 
    elif nums[mid] > val:
        return binarySearch2(nums, val, start, mid-1)
    else:
        return binarySearch2(nums, val, mid+1, end)
    
# Linear search is O(n)
# You go through every value in the array
# Binary search is O(log n)
# You go through the values diving n in half everytime, until we have 1 value.
# The number of steps you have is defined by how many times you have to divide 
# by two to get one -> this is the definition of Log(n) (with base 2, but we 
# drop the constant like that in Big-O analysis).