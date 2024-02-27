class Solution(object):
    def contains_duplicate(self, nums):
        
        for num in nums:
            if nums.count(num) > 1:
                return True