from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_1 = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[pointer_1] = nums[i]
                pointer_1 += 1
        return pointer_1
