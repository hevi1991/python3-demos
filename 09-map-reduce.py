# 1
def normalize(name):
    return name.lower().capitalize()

# 2
from functools import reduce
def prod(L):
    return reduce(lambda x,y: x*y, L)

# 3
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    lm = list(map(lambda n: DIGITS[n], s))

    i = lm.index('.')
    lm.pop(i)
    q = 10**i

    olm = reduce(lambda x, y: x * 10 + y, lm)
    olm = olm / q
    return olm