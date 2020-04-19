from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        1.遍历数组
        2.数组每个元素弹出并加1
        3.判断元素加1与10的大小，如果大于10，则把除余后的结果追加到新的数组中，如果小于10直接追加到新数组中
        4.反转新数组
        """
        flag = 1
        res = []

        for i in range(len(digits)):
            num = digits.pop() + flag
            if num >= 10:
                flag = 1
                res.append(num%10)
            else:
                flag = 0
                res.append(num)
                
        if flag == 1:
            res.append(flag)
        
        res.reverse()
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9, 9, 9]))
    print(s.plusOne([2, 3, 4]))