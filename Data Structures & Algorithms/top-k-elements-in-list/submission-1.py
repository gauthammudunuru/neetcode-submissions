from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        val = Counter(nums)
        bucket = [ [] for i in range(len(nums))]
        for key,v in val.items():
            bucket[v-1].append(key)
        for ind in range(len(bucket)-1, -1, -1):          
            for x in bucket[ind]:                
                out.append(x)                
                if len(out)==k:
                    return out

       
            
