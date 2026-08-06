class Solution:
    def isValid(self, s: str) -> bool:


        dabba = []
        
        open_bracket = "({["

        for i in s :
            if i in open_bracket:
                dabba.append(i)

            else:
                if len(dabba) == 0:
                    return False
                    
                
                top = dabba.pop()

                if i == ")" and top != "(":
                    return False 
                elif i =="]" and top != "[":
                    return False

                elif i == '}' and top != "{":
                    return False

        return len(dabba) == 0
                                             