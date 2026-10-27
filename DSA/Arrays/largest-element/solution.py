class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        
        for x in nums : 
            if x > largest :
                largest = x

        return largest