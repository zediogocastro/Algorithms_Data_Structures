from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            nums.append(nums[x])
        return nums
