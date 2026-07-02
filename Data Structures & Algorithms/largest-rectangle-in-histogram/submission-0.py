class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) #to handle non empty stack at the end of increasing bars
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n):
            if not stack or heights[i]>=heights[stack[-1]]:
                stack.append(i)
                continue
            right_ind = i
            while stack and heights[right_ind] < heights[stack[-1]]:             
                length = stack.pop()
                ind = stack[-1] if stack else -1
                max_area = max(max_area, (right_ind-ind-1)*heights[length] )
            stack.append(i)
        return max_area

