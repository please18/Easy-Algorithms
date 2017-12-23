# Given two strings s and t, write a function to determine if t is an anagram of s.
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1 = []
        list2 = []
        for i in s:
            list1.append(i)
            
        for j in t:
            list2.append(j)
            
        list1.sort()
        list2.sort()
        return list1 == list2
        
   ########### METHOD 2 #####################
    def isAnagram3(self, s, t):
      return sorted(s) == sorted(t)
