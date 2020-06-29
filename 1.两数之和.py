from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            pare = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[pare] = i
        return []

result = Solution().twoSum([1,2,3], 3)
print(result)