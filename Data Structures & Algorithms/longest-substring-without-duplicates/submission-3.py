class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Map = set()
        start = 0        
        max_l = 0
        for i in range(len(s)):
            while s[i] in Map:
                Map.remove(s[start])
                start+=1
            Map.add(s[i])
            max_l = max( max_l, i-start+1)
        return max_l