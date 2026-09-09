class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for chr in columnTitle: 
            result = result * 26 + (ord(chr)  - ord('A') + 1) 

        return result


    
