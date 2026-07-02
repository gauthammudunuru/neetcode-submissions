import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        valid = []
        st = 0
        end = max(piles)            
        while(st<=end):
            mid = (st+end)//2    
            if mid == 0:
                break
            total = 0
            for i in piles:
                total += math.ceil(i/mid)                
            if total<=h:
                valid.append(mid)
                end = mid-1
            else:
                st = mid+1
        
        return min(valid)