class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        e = len(matrix) - 1
        arr = None
        
        while s <= e:
            mid = (e + s) // 2
            first = matrix[mid][0]
            last = matrix[mid][-1]
            
            if first == target or last == target:
                return True
            if first < target and last > target:
                arr = matrix[mid]
                break
            if first > target:
                e = mid - 1
            elif last < target:
                s = mid + 1
        
        if not arr:
            return False

        s = 0
        e = len(arr) - 1
        while s <= e:
            mid = (e + s) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return False