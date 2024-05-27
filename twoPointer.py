def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currSum = array[left] + array[right]
        if currSum == targetSum:
            return [array[left], array[right]]
        elif currSum < targetSum:
            left += 1
        elif currSum > targetSum:
            right -= 1
    return []
        
print("TWO POINTER SUM:", twoNumberSum([3,5,-4,11,1,-1,6],10))

# TIME complexity = O( n )
# Space Complexity = O(n)