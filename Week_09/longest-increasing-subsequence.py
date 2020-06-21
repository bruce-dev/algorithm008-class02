#!/usr/local/anaconda3/bin/python

from typing import List

# Dynamic programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    lst = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(lst))