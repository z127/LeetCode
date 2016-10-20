Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
<pre>    
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
</pre>
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

##解题思路:
1.    给一个三角形数组，从上往下取相邻的数据,比如6只能取3，而不能去4,5只能取3,4，7只能取4.计算怎样取才能使取出的值最小。
2.    从下往上开始取，triangle[i][j]表示原数组,dp[i]为最后一层的第i个元素，第3层dp[i]=min(dp[i],dp[i+1])+triangle[2][i],
      根据第三层dp[i]求出第二层dp[i],最后求到第一层。返回dp[0]
        
