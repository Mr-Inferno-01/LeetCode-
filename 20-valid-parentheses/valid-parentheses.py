class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening_bracket  = "({["

        for o in s:
            if o in opening_bracket:
                stack.append(o)

            else:
                if len(stack) ==  0:
                    return False

                top = stack.pop()

                if o == ")" and top != "(":
                    return False
                    
                if o == "]" and top != "[":
                    return False

                if o == "}" and top != "{":
                    return False


        return len(stack) == 0