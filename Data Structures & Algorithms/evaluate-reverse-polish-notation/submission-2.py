from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = {
            '+': lambda x,y: x+y,
            '-': lambda x,y: x-y,
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y,
        }
        for t in tokens:
            if t in ops.keys():
                if len(stack) < 2: raise RuntimeError("Invalid tokens")
                second = stack.pop()
                first = stack.pop()
                stack.append(int(ops[t](first, second)))
            else: stack.append(int(t))
        return int(stack[0])