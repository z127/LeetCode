#-*- coding:utf-8 -*-
class Solution(object):
	
	#建立一个判断ij元素之间是否回文的数组。pali[0][0]=1 "a",pali[0][1]=1 "ab"
	def getpalidrome(self, s):
		pali=[[0 for col in range(len(s))] for row in range(len(s))]
		for j in range(len(s)):
			for i in range(j+1):
				if i==j:
					pali[i][j]=1
				elif s[i]==s[j]:
						if i+1==j or pali[i+1][j-1]==1:
							pali[i][j]=1
		return pali

	#根据传进来的字符串s，以及回文数组pali，来获取回文数组，如果是回文数组就添加进入结果中
	def getlist(self,s,start,pali,results,sol):
		if start==len(s):
			results.append(sol)
			return
		i=start 
		while i <len(s):
			if pali[start][i]==1 :
				#每次获得一个新的数据，根据函数传进来的sol-list,新建一个list。不然临时变量会修改数据。
				tmp=list(sol)
				tmp.append(s[start:i+1])
				self.getlist(s,i+1, pali,results,tmp)
			i=i+1

					

	#
	def partition(self,s):
		pali=self.getpalidrome(s)
		results=list(list()) 
		sol=list()
		self.getlist(s,0,pali,results, sol)
		return results







