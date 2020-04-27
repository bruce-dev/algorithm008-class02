#!/usr/local/anaconda3/bin/python

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and j != i:
                return [i, j]

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,3,4,5], 7))

