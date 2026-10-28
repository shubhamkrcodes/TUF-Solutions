class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]

        for i in nums:
            if i > largest:
                largest = i

        seclargest = None

        for j in nums:
            if j < largest:
                if seclargest is None or j > seclargest:
                    seclargest = j

        if seclargest is None:
            return -1

        return seclargest