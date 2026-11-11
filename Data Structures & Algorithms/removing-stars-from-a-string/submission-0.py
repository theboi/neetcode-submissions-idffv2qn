from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        li = deque()
        for ch in s:
            if ch != '*': li.append(ch)
            else: li.pop()
        return ''.join(list(li))
