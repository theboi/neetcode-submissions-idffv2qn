class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tab = set()
        largest = 0
        left = 0
        for right in range(len(s)):
            while s[right] in tab: 
                tab.remove(s[left])
                left += 1
            tab.add(s[right])
            largest = max(largest, len(tab))

        return largest