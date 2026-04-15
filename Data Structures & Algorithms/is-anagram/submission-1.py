class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tab = {}
        for l in s:
            if not l in tab: tab[l] = 1
            else: tab[l] = tab[l] + 1
        
        for l in t:
            if not l in tab or tab[l] == 0: return False
            else: tab[l] = tab[l] - 1
        
        for value in tab.values():
            if value != 0: return False
        return True