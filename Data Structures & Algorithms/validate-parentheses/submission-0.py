class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in pairs.values():
                stack.append(char)
                continue
            else:
                if len(stack) == 0 or stack[-1] != pairs[char]: return False
                stack.pop()
        return stack == []