class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab = {}
        for n in nums:
            if n in tab:
                return True
            tab[n] = True
        return False
