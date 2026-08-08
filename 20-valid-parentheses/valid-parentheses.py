class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening_bracket = "({["

        for i in s:
            if i in opening_bracket:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()

                if i == ")" and top != "(":
                    return False

                if i == "]" and top != "[":
                    return False

                if i == "}" and top != "{":
                    return False
        return len(stack) == 0