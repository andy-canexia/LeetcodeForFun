


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        pointer = 0
        for i in range(len(nums)):
            if nums[pointer] != nums[i]:
                pointer += 1
                nums[pointer] = nums[i]

        return pointer+1

