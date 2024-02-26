class Solution(object):
    # def reverse_string(self, s):

    #     return s.reverse()

    def reverse_string(self, s):
        
        reversed_string = []
        length = len(s)
        for letter in s:
            s.insert(length - 1, letter)
            length -= 1
        print(reversed_string)
        return reversed_string