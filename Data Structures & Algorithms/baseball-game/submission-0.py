from collections import deque
class Solution:
    def tryInt(self, s: str) -> int | None:
        try:
            return int(s)
        except (ValueError, TypeError):
            return None

    def calPoints(self, operations: List[str]) -> int:
        li = deque()
        for op in operations:
            maybeInt = self.tryInt(op)
            if maybeInt != None:
                li.append(maybeInt)
                continue
            if op == '+':
                li.append(li[-2]+li[-1])
            elif op == 'D':
                li.append(li[-1]*2)
            elif op == 'C':
                li.pop()
        return sum(li)