class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = dict()
        largest = 0
        left = 0
        for right in range(len(s)):
            if s[right] in mp: 
                left = max(mp[s[right]]+1, left)
            mp[s[right]] = right
            largest = max(largest, right-left+1)
        return largest