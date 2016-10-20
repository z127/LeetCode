#-*- coding:utf-8 -*-
class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		n=len(triangle)
		total=[None]*n
		 #将最后一段赋值，即4,1,8,3
		for  i in range(0,len(triangle[n-1]),1):
			total[i]=triangle[n-1][i]
			print total[i]
		#从下往上依次遍历，寻找最小值.
		for i in range(n-2,-1,-1):
			for j in range(0,len(triangle[i+1])-1,1):
				total[j]=triangle[i][j]+min(total[j],total[j+1])
				print "total" ,i,j,total[j],"\n"
		return total[0]

if __name__ == '__main__':
	b=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
] 
	print (Solution().minimumTotal(b))
