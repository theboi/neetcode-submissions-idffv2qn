from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        stack = deque() # will be a monotonically decreasing stack
        result = [0]*l

        for i in range(l):
            while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
                i_prev = stack.pop()
                result[i_prev] = i-i_prev
            stack.append(i)
        return result