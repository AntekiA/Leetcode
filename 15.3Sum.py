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

    
    class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        dic = {}
        tri = []
        nums.sort()
        st = 0
        le = len(nums)-1
        for i in range(le):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        while st < len(nums)  and nums[st] <= 0:
            le = len(nums)-1
            while (le - st) > 1 and nums[le] >= 0:
                tar = 0-nums[st]-nums[le]
                if tar in dic:
                    for u in dic[tar]:
                        if u != st and u != le :
                            if sorted([nums[st], nums[le], nums[u]]) not in tri:
                                tri.append(sorted([nums[st], nums[le], nums[u]]))
                le -= 1
            st += 1
                                
        return tri
