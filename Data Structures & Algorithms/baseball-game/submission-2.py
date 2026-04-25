class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for o in operations:
            if o == "+":
                top = st.pop()
                added = top + st[-1]
                st.append(top)
                st.append(added)
            elif o == "D":
                st.append(st[-1] * 2)
            elif o == "C":
                st.pop()
            else:
                st.append(int(o))
        return sum(st)