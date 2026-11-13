from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        lefts = [] # left bound exclusive
        rights = [] # right bound exclusive
        max_width = len(heights)
        for i in range(max_width):
            while len(stack) != 0 and heights[i] <= heights[stack[-1]]:
                stack.pop()
            lefts.append(-1 if len(stack) == 0 else stack[-1])
            stack.append(i)
        stack.clear()

        for i in range(len(heights)):
            j = max_width-i-1
            while len(stack) != 0 and heights[j] <= heights[stack[-1]]:
                stack.pop()
            rights.append(max_width if len(stack) == 0 else stack[-1])
            stack.append(j)
        rights = rights[::-1]

        print(lefts)
        print(rights)
        areas = [heights[i]*(rights[i] - lefts[i] - 1) for i in range(max_width)]
        return max(areas)
        
