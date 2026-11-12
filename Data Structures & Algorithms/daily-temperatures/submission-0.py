from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque() # will be a monotonically decreasing stack
        result = [-1]*len(temperatures)
        for i,t in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][1] < t:
                i_prev, t_prev = stack.pop()
                result[i_prev] = i-i_prev
            stack.append((i,t))
        for i,t in stack:
            result[i] = 0
        return result