# def createCounter():
#     def _all_iter(): #创建一个自然数序列，Iterator
#         n = 1
#         while True:
#             yield n
#             n = n + 1
#     it = _all_iter()
#     def counter():
#         return next(it) #利用迭代器的next函数
#     return counter

def createCounter():
    a = 0
    def counter():
        nonlocal a
        a += 1
        return a
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')