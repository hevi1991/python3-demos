def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    current = 0
    while(current < length):
        leftSum = sum(nums[0 : current])
        rightSum = sum(nums[current + 1:])
        if leftSum == rightSum:
            print(current,":",leftSum," vs ", rightSum)
            return current
        current += 1
    return -1

test = [1,7,3,6,5,6]
# test = [-1,-1,-1,0,1,1]
# test = [-1,-1,0,1,1,0]
index = pivotIndex(test)
print(index, " of " , len(test))