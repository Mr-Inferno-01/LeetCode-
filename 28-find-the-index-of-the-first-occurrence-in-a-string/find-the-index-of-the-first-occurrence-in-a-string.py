class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h =  len(haystack)
        n = len(needle)
         
        for i in range(h-n+1):
            match = True


            for j in range(n):
                if haystack[i+j] != needle[j]:
                    match = False
                    break

            if match:
                return i
        return -1