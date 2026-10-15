class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Traverse the array from last digit to first.
        for i in range(len(digits)-1,-1,-1):
            #if the current digit is less than 9 ,just increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits

            #If it is 9, it becomes 0 and the carry moves to the next digit
            digits[i] = 0


        # if all digits were 9(e.g., [9,9,9]) we need an extra digit at thr beginning
        return [1] + digits
        