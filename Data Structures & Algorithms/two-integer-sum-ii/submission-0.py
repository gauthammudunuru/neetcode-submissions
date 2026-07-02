class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Map = {}
        for i in range(len(numbers)):
            # print(target-numbers[i])
            if numbers[i] not in Map:
                Map[target-numbers[i]] = i
            else:
                return [ Map[numbers[i]]+1, i+1 ]
