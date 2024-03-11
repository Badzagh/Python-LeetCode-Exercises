class Solution(object):
    def move_zeroes(self, nums):
        
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)
        print(nums)
        return nums