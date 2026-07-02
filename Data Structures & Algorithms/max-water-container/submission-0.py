class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_cost = 0
        while start<=end:
            cost = min(heights[start],heights[end])*(end-start)
            max_cost = max(max_cost, cost)
            if heights[start] > heights[end]:
                end-=1
            else:
                start+=1
        return max_cost