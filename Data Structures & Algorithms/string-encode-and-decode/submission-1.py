class Solution:

    def encode(self, strs: List[str]) -> str:        
        s = ""
        for i in strs:
            l = len(i)
            s+=str(l)+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0
        start = 0
        while i<len(s):                                       
            if s[i]!="#":
                i+=1
            elif s[i]=="#":                
                l = int(s[start:i])
                strs.append(s[i+1:i+l+1])               
                i=l+i+1
                start=i
        return strs
