#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if (not s) or (not wordDict):
            return  False
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        for i in range(len(s)):
            for k in range(i+1,len(s)+1):
                if dp[i] and s[i:k] in wordDict:
                    dp[k]=True
                    print "i is %d,dp %d is %d and %s"%(i,k,dp[k],s[i:k]) 
        return dp[len(s)]








if __name__=="__main__":
    c=Solution()
    b=c.wordBreak("sdadsada",set(['sda','ds','ada']))
    print b


