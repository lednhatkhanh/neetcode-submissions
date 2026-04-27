class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        self.mergeSort(nums1,0,len(nums1) - 1)
    def mergeSort(self, arr, s, e):
        if (e - s + 1) <= 1:
            return
        
        mid = (s + e) // 2
        self.mergeSort(arr, s, mid)
        self.mergeSort(arr, mid + 1, e)

        return self.mergeArr(arr, s, mid, e)
    def mergeArr(self, arr, s, m, e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]
        l = 0
        r = 0
        k = s

        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                arr[k] = L[l]
                l += 1
            else:
                arr[k] = R[r]
                r += 1
            k += 1
        
        while l < len(L):
            arr[k] = L[l]
            l += 1
            k += 1
        while r < len(R):
            arr[k] = R[r]
            r += 1
            k += 1
