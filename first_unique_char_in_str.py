class Solution(object):
    def first_unique_char_in_str(self, s):
        
        my_list = list(s)
        my_set = set(s)
        my_list_of_set = list(my_set)

        is_different = len(my_list) != len(my_list_of_set)

        if is_different:
            for letter in s:
                if s.count(letter) > 1:
                    s = s.replace(letter, '')
            if len(s) > 0:
                return my_list.index(s[0])
            else:
                return -1
        else:
            return 0