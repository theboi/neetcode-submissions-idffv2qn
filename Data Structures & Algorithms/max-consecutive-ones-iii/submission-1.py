from collections import Counter
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        acc = Counter()
        left = 0
        for right in range(len(nums)):
            acc.update([nums[right]])
            while acc[0]>k:
                acc.subtract([nums[left]])
                left += 1
            res = max(acc[1] + min(acc[0], k), res)
        return res