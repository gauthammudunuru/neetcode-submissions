class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) #to handle non empty stack at the end of increasing bars
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n):
            
            while stack and heights[i] < heights[stack[-1]]:             
                length = stack.pop()
                ind = stack[-1] if stack else -1
                max_area = max(max_area, (i-ind-1)*heights[length] )
            stack.append(i)
        return max_area

