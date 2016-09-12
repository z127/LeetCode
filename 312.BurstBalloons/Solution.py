#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[1]+[i for i in nums if i>0]+[1]
        n=len(nums)
        dp=[[0]*n for x in xrange(n)]
        #设定砖块大小。从最小为2 开始叠加
        for k in range(2,n):
        	#从左往右开始遍历计算每个小砖块的dp值
        	for left in xrange(0,n-k):
        		right=left+k
        		#根据题设，nums[left]*nums[i]*nums[right]，计算从左往右选定一个i值，来计算dp[left][right]
        		for i in xrange(left+1,right):
        			dp[left][right]=max(dp[left][right],nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]



if __name__ == '__main__':
   c=Solution()
   print (c.maxCoins([3, 1, 5, 8]))


