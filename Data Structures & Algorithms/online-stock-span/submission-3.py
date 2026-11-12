from collections import deque
class StockSpanner:
    def __init__(self):
        self.days = []
        self.stack = deque()
        return None

    def next(self, price: int) -> int:
        self.days.append(price)
        i = len(self.days)-1
        while len(self.stack) != 0 and price >= self.days[self.stack[-1]]:
            self.stack.pop()
        left_i = -1 if len(self.stack) == 0 else self.stack[-1]
        self.stack.append(i)
        return i - left_i
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)