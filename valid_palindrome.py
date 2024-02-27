class Solution(object):
    def is_palindrome(self, s):
        # new_s = s.lower().replace(" ", "").replace("!","").replace("?","").replace(".","").replace(",","").replace(":","")
        
        new_s = ""
        s = s.lower()

        for letter in s:
            if letter.isalpha():
                new_s += letter

        list_of_string = list(new_s)
        list_of_string_reversed = list(new_s)
        list_of_string_reversed.reverse()

        return list_of_string == list_of_string_reversed