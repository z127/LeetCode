Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

##解题思路:
        1.上述题目叙述了给一个字符串,将一个字符串分解成回文字符串，能够分解成几种形式。
        2.首先判断字符串中有几种回文形式，pali[i][j]表明字符串从i到j是否是回文。
          如果两个字符i，j相等,判断只需要两种情况，如果j=i+1，表明该字符串是回文的，如果结果不是，判断pali【i+1】【j-1】是否是1就可以了，如果是1，就pali【i】【j】也是1.
        3.最后用递归的方法，来判断整个字符串有几种划分方式。
        4.最后要注意因为传进去的list变量sol的本质是一个引用，所以每次得到一个数据的时候都要根据传进来的list，new一个新的list。不要会导致list混乱。
        
