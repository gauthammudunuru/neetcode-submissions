class Solution:
    def isAlphaNumeric(self, char):
        a,b,c = False, False, False
        print(char)
        if ord(char)>=ord("a") and ord(char)<=ord("z"):
            a = True
        if ord(char)>=ord("A") and ord(char)<=ord("Z"):
            b = True
        if ord(char)>=ord("0") and ord(char)<=ord("9"):
            c = True
        print(a,b,c, a or b or c)
        return a or b or c
        
    def isPalindrome(self, s: str) -> bool:
        # print(ord("a"), ord("z"), ord("A"),ord("Z"), ord("0"), ord("9"))
        start=0
        end=len(s)-1
        while start<=end:
            # print(start, end, s[start], s[end])
            if not self.isAlphaNumeric(s[start]):
                start+=1
                continue
            if not self.isAlphaNumeric(s[end]):
                end-=1
                continue
            if s[start].lower() != s[end].lower():
                return False
            else:
                # print(s[start], s[end])
                start+=1
                end-=1
        return True