class Solution:
    def isPalindrome(self, s: str) -> bool:
        pall  = []
        for i in s:
            if i.isalnum():
                pall.append(i)

        chars = ''.join(pall).lower()

        if chars[::-1] == chars:
            return True
        else: 
            return False

        
