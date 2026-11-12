from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque() # monotonic increasing stack
        max_area = 0
        max_width = len(heights)
        for i in range(max_width):
            i_leftmost = i
            while len(stack) != 0 and heights[i] <= stack[-1][1]:
                i_prev, h_prev = stack.pop()
                i_leftmost = i_prev
                max_area = max(max_area, h_prev * (i-i_prev))
            stack.append((i_leftmost,heights[i]))
        while len(stack) != 0:
            i_prev, h_prev = stack.pop()
            max_area = max(max_area, h_prev * (max_width-i_prev))
        return max_area
