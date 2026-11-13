class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tab = {}
        for i in range(len(nums)):
            if nums[i] in tab and i-tab[nums[i]]<=k: return True
            tab[nums[i]] = i
        return False