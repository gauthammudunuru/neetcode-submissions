class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Map = set(nums)

        MaxL = min(1, len(nums))
        for i in Map:
            if i-1 not in Map:
                val = i
                L = 1
                while val+1 in Map:
                    val+=1
                    L+=1
                    MaxL = max(MaxL,L)
        return MaxL