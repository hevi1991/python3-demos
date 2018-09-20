import math
def quadratic(a, b, c):
    x = -4 * a * c + b * b
    x = math.sqrt(x)
    x , y = x , -x
    def getSquareRoot(z):
        return (z - b) / 2 / a
    x = getSquareRoot(x)
    y = getSquareRoot(y)
    return x, y

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))