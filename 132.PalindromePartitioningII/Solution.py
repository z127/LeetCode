 def minCut(self,s):
        #len(s)+1 是因为1+dp[j+1]的时候会溢出，为了防止溢出dp的length+1.经验证 最后不影响结果
        dp=[len(s)- i for i in range(len(s)+1)]
        pali=[[0 for  i  in range(len(s))] for j in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j  in range(i,len(s)):
                    #判断是否为回文
                      if s[i]==s[j] and (((j-i)<2) or pali[i+1][j-1]==1 ):
                                pali[i][j]=1
                                #如果ij为会问的话，则i到j切割，只需要一刀
                                dp[i]=min(1+dp[j+1],dp[i])

        return dp[0]-1
