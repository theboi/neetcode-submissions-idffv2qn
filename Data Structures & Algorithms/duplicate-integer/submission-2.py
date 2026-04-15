class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = set()
        for n in nums:
            if n in tab:
                return True
            tab.add(n)
        return False
