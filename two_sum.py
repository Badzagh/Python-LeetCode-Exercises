class Solution(object):
    def two_sum(self, nums, target):
        for num in nums:
            if target - num != num:
                if nums.count(target - num) != 0:
                    return [nums.index(num), nums.index(target - num)]
            else:
                if nums.count(target - num) != 1:
                    return [nums.index(num), nums.index(num, nums.index(num) + 1, len(nums))]