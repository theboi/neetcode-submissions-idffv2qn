class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        tab = [0]*n
        tab[0] = 1
        tab[1] = 2
        i = 2
        while i != n:
            tab[i] = tab[i-1] + tab[i-2]
            i += 1
        return tab[n-1]