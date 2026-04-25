class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in pairs:
                if not st or st[-1] != pairs[c]:
                    return False
                else:
                    st.pop()
            else:
                st.append(c)
        return not st
