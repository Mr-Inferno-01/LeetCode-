class Solution:
    def longestCommonPrefix(self, s: list[str]) -> str:
        if not s:
            return ""



        for i in range(len(s[0])):
            char = s[0][i]

            for j in range(1,len(s)):
                if i == len (s[j]) or s[j][i] != char:
                    return s[0][:i]

        
        return s[0]