class Solution(object):
    def valid_anagram(self, s, t):
        
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        return s_list == t_list