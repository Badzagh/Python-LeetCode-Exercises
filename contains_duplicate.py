class Solution(object):
    def contains_duplicate(self, nums):
        
        my_set = set(nums)
        my_list = list(my_set)
        my_list.sort()
        nums.sort()
        is_different = my_list != nums
        return is_different