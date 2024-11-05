import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[r] = nums[r-1]
                left += 1
        return left


# Write unit test for the above

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([1,1,1,1,1,2,2]))
    print(s)

