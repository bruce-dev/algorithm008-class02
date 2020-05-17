class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##用切片的方法：k就是将nums的最后k个数放在nums的开始位置即可
        lenth = len(nums)
        nums[:] = nums[lenth-k:]+nums[:lenth-k]
