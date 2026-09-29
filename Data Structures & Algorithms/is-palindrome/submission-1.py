class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_s = [ch.lower() for ch in s if ch.isalnum()]
        return f_s == f_s[::-1]
                 
        




        