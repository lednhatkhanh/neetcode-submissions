import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quicksort(points, 0, len(points) - 1, k)
        return points[:k]

    def quicksort(self, arr, s, e, k):
        if e - s + 1 <= 1:
            return

        pivotId = random.randint(s, e)
        arr[e], arr[pivotId] = arr[pivotId], arr[e]

        dPivot = arr[e][0] ** 2 + arr[e][1] ** 2
        left = s

        for i in range(s, e):
            dI = arr[i][0] ** 2 + arr[i][1] ** 2

            if dI < dPivot:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        arr[left], arr[e] = arr[e], arr[left]

        if left > k:
            self.quicksort(arr, s, left - 1, k)
        elif left < k:
            self.quicksort(arr, left + 1, e, k)
