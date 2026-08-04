class Solution:
    def romanToInt(self, d: str) -> int:
        roman_no = {
            'I' :1,
            'V' :5,
            'X' :10,
            'L' :50,
            'C' :100,
            'D' :500,
            'M' :1000
        }

        total = 0
        n = len(d)

        for i in range(n):
            if i < n -1 and roman_no[d[i]] < roman_no[d[i+1]]:
                total -= roman_no[d[i]]
            
            else:
                total += roman_no[d[i]]

        return total