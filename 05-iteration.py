def findMinAndMax(L):
    if L == []:
        return (None, None)
    maxValue = None
    minValue = None
    for i,d in enumerate(L):
        if i == 0:
            maxValue = d
            minValue = d
        if d > maxValue:
            maxValue = d
        if d < minValue:
            minValue = d
    return (minValue, maxValue)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')