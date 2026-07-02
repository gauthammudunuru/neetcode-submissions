class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(0,len(nums)):
            val = target-nums[i]
            if val in Map:
                return [Map[val], i]
            else:
                Map[nums[i]] = i
              
