def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
                return [ potentialMatch, num]
        else:
            nums[num] = True
    return []
        
print("HASHMAP", twoNumberSum([3,5,-4,11,1,-1,6],10))

# TIME complexity = O( n )
# Space Complexity = O(n)