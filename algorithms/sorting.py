# Bubble sort - compares adjacent pairs and swaps every time until sorted
# Worst case is O(n^2) this happens when its reverse sorted
# Best case is O(n) this happens when its sorted (due to the sorted boolean)
def bubblesort(arr):
    sorted = False
    for i in range(len(arr)): # go through whole array
        for j in range(len(arr)-1-i): #go through the array up to n-1-i 
        # (bc we access arr[j+1] and we already know the last i elements will 
        # be sorted after our i'th passing.) 
            sorted = True
            print("comparing", arr[j], "and", arr[j+1])
            if arr[j] > arr[j+1]:
                sorted = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if sorted: return arr # optimized to return if its sorted after one pass
        print("after one passing", arr)
    return arr

# Selection sort - bubble sort brings the largest elements to the end slowly, 
# in that sense, selection sort is the inverse of that (not exactly since we 
# conpare pairs) in the sens that it always brings the smallest down to the front. 
# Selection sort basically finds the smallest in the subarray and start to sort 
# the first half of the array by swapping it to its right location.  
# Runtime: O(n^2) 
def selectionsort(arr):
    for i in range(len(arr)): # the whole array O(n)
        min = i
        curr = i + 1
        while curr < len(arr): # starting from i+1 to the end of the array 
            # this is still considered O(n) 
            if arr[curr] < arr[min]:
                min = curr
            curr += 1
        arr[i], arr[min] = arr[min], arr[i]
        print(i+1,":",arr)

# insertion sort - keeps the left partition of the array sorted and looks
# directly right of the partition to see if its larger the last elemented 
# in the sorted partition. If it is, it keeps swapping to the left until it
# determines the right place to insert the new element.
# Worst case you shift every thing over to insert for every element. therefore
# O(n^2)
def insertionsort(arr):
    for i in range(len(arr)): # O(n)
        j = i + 1  # adj to the partion and the elem we will be inserting
        while j - 1 >= 0 and j < len(arr) and arr[j] < arr[j-1]: # while index 
            # is valid and j needs to have things shifted over to insert.
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1 # keep going further left to check if the item is at the right place
        print(arr)

# merge sort - uses the classic divide and conquer to sort an array
# it splits the array into half util it is comparing two elements.
# for each of those left and right halves, it sorts them at each level
# for instance: for array [1, 4, 8, 5]
# [1, 4] and [8, 5]
# then [1] and [4] as well as [8] and [5]
# one and four get merged as [1, 4] and returned to be comapred to [5, 8]
# both of those are compared to return [1, 4, 5, 8]
# we'll need a recursive mergesort, and a helper function to sort the array
# runtime: O(nlogn) this is becuse it splits it in half till base case of 1 
# this is the definition of log (base 2) n. and for each of these n, we 
# compare the elements which are of size n. The interesting thing about mergesort 
# is that it has a great runtime but it's always O(nlogn) where as bubble sort 
# that has a worse big O runtime of O(n^2) will sometimes outperform it. For intance
# if it's already sorted, bubble sort will do O(n) but mergesort will still do O(nlogn)
def mergesort(arr):
    if len(arr) < 2: return arr 
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(arr1, arr2):
    if not arr1 or not arr2: return arr1 or arr2
    len1, len2 = len(arr1), len(arr2)
    i, j = 0, 0, 
    arr = []
    print("arr1:", arr1, "arr2:", arr2)
    while i < len1 and j < len2:
        print(arr1[i], "vs", arr2[j])
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    if i < len1:
        arr.extend(arr1[i:])
    if j < len2:
        arr.extend(arr2[j:])
    return arr

# quicksort - Quicksort works by repeatedly splitting the array to 
# partitions around the pivot--meaning, it'll organize the subarr/arr 
# to less than pivot and greater than pivot. this essentially ensures
# that the pivot is at the exact location it needs to be in after the 
# partition. every element will get to be the pivot and therefore 
# find it's perfect spot. partition is what picks the pivot (the last
# element in the subarray) and puts everything less then before the pivot
# and everything greater than after the pivot, puts the pivot in the right 
# place. then it does the partition (pick pivot and rearrange) for each of  
# the subarrays left and right of the partition. 
# Runtime: O(n^2) -> if you pick the wrong pivot (greatest element or 
# smallest element) you keep doing partitons unevenly. however this would 
# be if your array is sorted in some order (ascending/descending)
# more often, you dont have to worry about this worst case. it's often O(nlogn)
# bc you split it each time and you do a factor or n comparisions for each logn
# space complexity is O(logn) as you do logn recursion calls. 
 
def quicksort(arr, begin, end):
    if begin >= end: return 
    pivot = partition(arr, begin, end) # the place to partition around
    quicksort(arr, begin, pivot - 1) # run partition on the left side of pivot 
    quicksort(arr, pivot + 1, end) # run partition on the right side of pivot

def partition(arr, begin, end):
    pivot = end # the last element is our pivot
    i, j = begin - 1 , begin # i always will start off index, j will be where to begin
    while j < pivot: # as long we dont see the pivit 
        if arr[j] <= arr[pivot]: 
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] 
        j += 1
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1


# tim sort