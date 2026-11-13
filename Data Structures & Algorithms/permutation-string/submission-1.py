from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        key = Counter(s1)
        tab = Counter()
        left = 0
        for right in range(len(s2)):
            if right-left>=k:
                tab.subtract(s2[left])
                left += 1
            tab.update(s2[right])
            if tab == key: return True
        return False