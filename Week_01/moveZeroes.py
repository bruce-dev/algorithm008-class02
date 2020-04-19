from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1.遍历数组
        2.判断数组元素是否为0，如果为0，则删除当前元素，并在数组末尾添加0
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)

        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))    
