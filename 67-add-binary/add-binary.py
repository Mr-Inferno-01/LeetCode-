class Solution:
    def addBinary(self, a: str, b: str) -> str:
        char =  int(a,2) + int(b,2)
        return bin(char)[2:]