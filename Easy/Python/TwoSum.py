class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            item = nums[i]
            if target-item in prev:
                return [prev[target-item], i]
            else:
                prev[item]=i
