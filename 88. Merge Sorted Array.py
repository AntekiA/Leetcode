class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while len(nums1) != m:
            nums1.pop()
        while i < m and j < n:
            if nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                m += 1
                j += 1
                continue
            i += 1
        while j < n:
            i += 1
            nums1.insert(i, nums2[j])
            j += 1
       
class Solution_short:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=nums1[0:m]
        nums1.extend(nums2)
        nums1.sort()
