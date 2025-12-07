def findLIS(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
        
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if (nums[i - 1] < nums[i]):
            dp[i] = dp[i - 1] + 1
            
    return max(dp)

s = [int(x) for x in input().split()]
print(findLIS(s))
