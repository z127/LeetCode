Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.



## 解题思路
1.      只可以用删除字符的方法从第一个字符串变换到第二个字符串，求出一共有多少种变换方法
2.      这是一个动态规划问题，创建一个len(s)*len(T)的二维数组，dp[i][0]=1表示0到i的字符串的中只有一种
        方法也就是全部删除才能变成空串，如果字符s[i]==t[j],表示有两种方式，dp[i][j]=dp[i-1][j-1]+dp[i-1][j],当前这个字母即可以保留也可以抛弃，
        所以变换方法等于保留这个字母的变换方法加上不用这个字母的变换方法
3.      如果s[i]!=t[j],那么dp[i][j]=dp[i-1][j]，意思是如果当前字符不等，那么就只能抛弃当前这个字符
4.      dp[len(t)+1][len(s)+1] 表示收集前面n个字符的结果。
