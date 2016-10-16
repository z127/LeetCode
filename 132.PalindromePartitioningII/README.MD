Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

##解题思路
1.      上述题目叙述了给一个字符串，找出最少的回文子串划分方式
2.      对于一个字符串s，首先先初始化回文子串，也就是最简单方式-每一个字母切割一次,dp[i]表示数字i到n之间的最少回文子串。然后创立一个回文二维数组pali[i][j],表示ij字符串是回文的.
        然后从后往前去判断字符串pali[i][j]是否是回文,如果是回文判断dp[i]=min(1+dp[j],dp[i]).因为前面回文字符串是回文所以只要一刀。然后逐一遍历整个s，返回的d[0]-1。
