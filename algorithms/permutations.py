# There was this interesting question I did on an interview
# it really stumpted me, and I found the most elegent code out on
# geeksforgeeks on it. 

# Question: leetcode # 46. Permutations
# Given a collection of distinct integers, return all possible permutations.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def getperms(num, l, r, soln):
            if l == r: 
                soln.append(num[:]) 
                return
            for i in range(l, r+1):
                num[i], num[l] = num[l], num[i]
                getperms(num, l+1, r, soln)
                num[i], num[l] = num[l], num[i]

        soln = []
        getperms(nums, 0, len(nums)-1, soln)
        return soln