class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        track = 0
        sandwiches.reverse()

        while sandwiches:
            if track == len(queue):
                return track
            st = queue.popleft()
            if st == sandwiches[-1]:
                sandwiches.pop()
                track = 0
                continue
            else:
                track += 1
                queue.append(st)
        return len(queue)