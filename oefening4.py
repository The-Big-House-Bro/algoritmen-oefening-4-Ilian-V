def countTargetPairs(nums, target):
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                count += 1
                
    return count
