

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, num in enumerate(nums):
            n = target - num
            if n not in result:
                result[num] = index
            else:
                return [result[n], i]
