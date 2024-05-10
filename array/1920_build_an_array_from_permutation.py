def buildArray(nums):
    ans = []
    for num in nums:
        ans.append(nums[num])
    return ans

nums = [0, 2, 1, 5, 3, 4]
print(buildArray(nums))