class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for s in sandwiches:
            if counter[s] > 0:
                counter[s] -= 1
            else:
                break
        return sum(counter.values())