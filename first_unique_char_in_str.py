class Solution(object):
    def contains_duplicate(self, nums):
        
        my_list = list(s)
        my_set = set(s)
        my_list_of_set = list(my_set)

        is_different = len(my_list) != len(my_list_of_set)
        print(my_list)
        print(my_list_of_set)
        print([x for _,x in sorted(zip(my_list,my_list_of_set))])
        if is_different:
            
            for letter in my_list:
                if my_list.count(letter) < 2:
                    return my_list.index(letter) 
            return -1
        else:
            return 0