class Solution(object):
    def valid_parentheses(self, s):
        
        # firts_open = "("
        # firts_close = ")"
        # second_open = "{"
        # second_close = "}"
        # third_open = "["
        # third_close = "]"

        
        
        # if s[0] == firts_open or s[0] == second_open or s[0] == third_open:
        #     print(s[0])
        # else:
        #     print("19LINE")
        #     return False
        # if s[len(s) - 1] == firts_close or s[len(s) - 1] == second_close or s[len(s) - 1] == third_close:
        #     print(s[len(s) - 1])
        # else:
        #     print("24LINE")
        #     return False

        # if s.count(firts_open) != s.count(firts_close):
        #     print("28LINE")
        #     return False
        # else:
        #     if firts_open in s and firts_close in s:
        #         if s.index(firts_open) > s.index(firts_close):
        #             print("33LINE")
        #             return False
        #         if s.index(firts_close) - s.index(firts_open) != 1 and (s.index(firts_close) - s.index(firts_open)) % 3 != 0:
        #             print("36LINE")
        #             print(s.index(firts_close) - s.index(firts_open) != 1 and (s.index(firts_close) - s.index(firts_open)) % 3 != 0)
        #             return False

        # if  s.count(second_open) != s.count(second_close):
        #     print("40LINE")
        #     return False
        # else:    
        #     if second_open in s and second_close in s:
        #         if s.index(second_open) > s.index(second_close):
        #             print("45LINE")
        #             return False
        #         if s.index(second_close) - s.index(second_open) != 1 and (s.index(second_close) - s.index(second_open)) % 3 != 0:
        #             print("48LINE")
        #             return False
        #         if s[s.index(second_open) + 1] == firts_close or s[s.index(second_open) + 1] == third_close:
        #             print("52LINE")
        #             return False

        # if  s.count(third_open) != s.count(third_close):
        #     print("56LINE")
        #     return False
        # else:
        #     if third_open in s and third_close in s:
        #         if s.index(third_open) > s.index(third_close):
        #             print("61LINE")
        #             return False
        #         if s.index(third_close) - s.index(third_open) != 1 and (s.index(third_close) - s.index(third_open)) % 3 != 0:
        #             print("64LINE")
        #             return False

        # return True

        # s = s.replace("()", "").replace("{}", "").replace("[]", "")
        # s = s.replace("{}", "").replace("[]", "").replace("()", "")
        # s = s.replace("[]", "").replace("()", "").replace("{}", "")
        while ("()" in s or "{}" in s or "[]" in s):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        print(s)
        if s == "":
            return True