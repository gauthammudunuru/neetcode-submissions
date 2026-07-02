from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1>n2:
            return False
        
        target, window = Counter(s1), Counter(s2[:n1])
        if window == target:
            return True
            
        start = 0
        for i in range(n1,n2):
            window[s2[start]] -= 1
            if window[s2[start]] == 0:
                window.pop(s2[start])
            window[s2[i]] +=1
            start+=1
            if window == target:
                return True

        return False