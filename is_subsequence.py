class Solution(object):
    def is_subsequence(self, s, t):
       
        new_str= ""
        for letter in t:
            if s.count(letter) == 0:
                t = t.replace(letter, "")
                print(t)
        if s == t:
            return True
        else: 
            if s in t:
                return True
            else:
                for letter in t:
                    if t.count(letter) > 1 and t.count(letter) != s.count(letter):
                        t = t.replace(letter, "", t.count(letter) - s.count(letter))
                if s == t:
                    return True
                else:
                    return False