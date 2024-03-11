class Solution(object):
    def happy_number(self, n):

        # number = 0
        # seen = set()
        # while n != 1 and n not in seen:
        #     seen.add(n)
        #     for digit in str(n):
        #         number += int(digit) ** 2
        #     n = number
        # return n == 1
        
        seen = set()  

        while n != 1:
            seen.add(n)
            next_num = sum(int(digit) ** 2 for digit in str(n))
            n = next_num

        return n == 1