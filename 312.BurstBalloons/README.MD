Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
coins =  3x1x5      +  3x5x8    +  1x3x8      + 1x8x1   = 167
  
##解题思路
    1.该题是一道动态规划题，dp[l][r]表示（l,r）范围内扎破气球的最大硬币数,不含边界.
    状态转移方程为 left<i<right dp[left][right]=max(dp[left][i]+nums[l]*nums[i]*nums[r]+dp[i][right],dp[left][right])
    2.要计算dp[left][right]需要根据题设算出最小的dp[left][right],k=right-left=2,随着k增加，right-left逐渐增大。dp[0][n-1]求出为最大值
