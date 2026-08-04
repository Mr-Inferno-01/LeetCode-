class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Array ko lexicographically (alphabetically) sort karte hain
        strs.sort()
        
        # Pehla aur aakhri string lete hain
        first = strs[0]
        last = strs[-1]
        
        i = 0
        # Dono strings mein jab tak characters match kar rahe hain, aage badhein
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        # Common prefix slice return kar dein
        return first[:i]