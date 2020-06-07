#!/usr/local/anaconda3/bin/python

class Solution:
    def climbStairs(self, n: int) -> int:
        climb = {}
        
        climb[0] = 0
        #上第一阶台阶有1种方法
        climb[1] = 1
        # 上第二阶台阶有两种方法
        climb[2] = 2

        # 以此类推，上n阶台阶为上n-1阶台阶和n-2阶台阶的方法 
        for i in range(3, n+1):
            climb[i] = climb[i-1] + climb[i-2]
        return climb[n]


if __name__ == "__main__":
    s = Solution()
    print(int(s.climbStairs(4)))