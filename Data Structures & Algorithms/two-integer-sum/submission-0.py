class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_nums = {}
        for i in range(len(nums)):
            want = target-nums[i]
            if want in target_nums.keys(): 
                return [target_nums[want], i]
            target_nums[nums[i]] = i
            
