class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0]*26
        for l in s:
            alpha[ord(l)-97] += 1
        for l in t:
            alpha[ord(l)-97] -= 1
        return all(x == 0 for x in alpha)