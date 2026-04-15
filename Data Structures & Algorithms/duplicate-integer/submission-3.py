class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = set(nums)
        return len(tab) != len(nums)