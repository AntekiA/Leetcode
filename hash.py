nums = [3, 2, 3, 4, 4, 5, 3]
num_dict = dict()
for num_ndx in range(len(nums)):
    if nums[num_ndx] in num_dict:
        num_dict[nums[num_ndx]].append(num_ndx)
    else:
        num_dict[nums[num_ndx]] = [num_ndx]
print(num_dict)
