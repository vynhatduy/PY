import math
def la_so_fibonacci(n):
    x = 5 * n * n + 4
    y = 5 * n * n - 4
    return math.isqrt(x) ** 2 == x or math.isqrt(y) ** 2 == y
print(la_so_fibonacci(8))