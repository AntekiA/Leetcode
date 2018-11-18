class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        tri = []
        le = len(nums)
        for i in range(le):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        for i in range(le):
            for j in range(le):
                if i != j:
                    tar = 0-nums[i]-nums[j]
                    if tar in dic:
                        for u in dic[tar]:
                            if u != i and u != j:
                                if sorted([nums[i], nums[j], nums[u]]) not in tri:
                                    tri.append(sorted([nums[i], nums[j], nums[u]]))
                                
        return tri
