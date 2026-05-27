class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ')': '(', ']' :'['}
        st = []

        for c in s:
            if c == '{' or c =='[' or c == '(':
                st.append(c)
            else:
                if len(st) == 0:
                    return False
                char = st[-1] 
                if char == pairs[c]:
                    st.pop()
                else:
                    return False
        
        return len(st) == 0
