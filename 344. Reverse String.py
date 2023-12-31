# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r  = 0 , len(s) -1
        while  l < r:
            s[l],s[r] = s[r],s[l]
            l,r = l +1 , r - 1
        

# SOLUTION #2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []

        for l in s:
            stack.append(l)
        
        i = 0
        while i < len(s):
            s[i] = stack.pop()
            i += 1 
        return s
        
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(l,r):
            if l < r:

                s[l],s[r] = s[r], s[l]
                reverse(l + 1, r -1)
        reverse(0,len(s) -1)
