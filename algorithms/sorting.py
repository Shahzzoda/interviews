# Bubble sort - compares adjacent pairs and swaps every time until sorted
# Worst case is O(n^2) this happens when its reverse sorted
# Best case is O(n) this happens when its sorted. I didn't implemented in 
# my code but you can go through it once to see if it needs swapping, that's O(n).
def bubblesort(arr):
    for i in range(len(arr)): # go through whole array
        for j in range(len(arr)-1-i): #go through the array up to n-1-i 
        # (bc we access arr[j+1] and we already know the last i elements will 
        # be sorted after our i'th passing.) 
            print("comparing", arr[j], "and", arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("after one passing", arr)

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
# quick sort



# tim sort