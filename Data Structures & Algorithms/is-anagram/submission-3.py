class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        seen_s = {}
        for i in range(0, len(s)):
            if s[i] not in seen_s:
                seen_s[s[i]] = 1
            else:
                seen_s[s[i]]+=1
        for i in range(0,len(t)):
            if t[i] not in seen_s:
                return False
            else:
                seen_s[t[i]]-=1

            if seen_s[t[i]]<0:
                return False
        return True