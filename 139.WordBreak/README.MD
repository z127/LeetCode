Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

##解题思路:
1.    上述题目叙述了将字符串分割为字典含有的几个子字符串，分割成功则返回true，否则为false  
2.    一个字符串S，它的长度为N，如果S能够被“字典集合”（dict）中的单词拼接而成，那么所要满足的条件为:
                F(0, N) = F(0, i) && F(i, j) && F(j, N);
        
