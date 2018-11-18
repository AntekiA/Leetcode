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

    
    class Solution_best:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
