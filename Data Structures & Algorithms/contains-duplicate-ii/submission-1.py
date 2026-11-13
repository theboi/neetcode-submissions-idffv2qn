class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tab = set()
        left = 0
        for right in range(len(nums)):
            if right-left>k:
                tab.remove(nums[left])
                left += 1
            if nums[right] in tab: return True
            tab.add(nums[right])
        return False