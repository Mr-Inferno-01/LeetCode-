class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        opening_bracket  =  "([{"

        for i in s:
            if i in opening_bracket:
                stack.append(i)

            else:
                if len(stack) == 0 :
                    return False

                top_bracket = stack.pop()

                if i == ")" and top_bracket != "(":
                    return False

                if i == "]" and top_bracket != "[":
                    return False
                        
                if i == "}" and top_bracket != "{":
                    return False

        return len(stack) == 0
