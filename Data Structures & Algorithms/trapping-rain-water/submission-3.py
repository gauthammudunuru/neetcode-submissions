class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        out = 0
        left = 0
        right = 0
        while start<end:                        
            if height[start]<height[end]:
                if height[start]>left:
                    left=height[start]                    
                else:
                    out+=left-height[start]
                start+=1
            else:
                if height[end]>right:
                    right=height[end]                 
                else:
                    out+=right-height[end]
                end-=1
        return out