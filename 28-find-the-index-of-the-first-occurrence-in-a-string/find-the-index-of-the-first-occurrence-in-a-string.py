class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h =  len(haystack)
        n = len(needle)
         
        for i in range(h-n +1):
            is_found = True


            for j in range(n):
                if haystack[i+j] != needle[j]:
                    is_found = False
                    break

            if is_found:
                return i
        return -1