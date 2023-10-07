def fibonacciRecursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def sumFibonacciRecursive(n):
    sum = 0
    for i in range(1, n+1):
        sum += fibonacciRecursive(i)
    return sum


def sumFibonacciIterative(n):
    sum = 0
    if n == 0:
        return 0
    a, b = 0, 1
    while n > 0:
        sum += a
        a, b = b, a + b
        n -= 1
    return sum




print("sử dụng đệ quy")
n = int(input("Nhập số lượng số Fibonacci cần tính: "))
sum_recursive = sumFibonacciRecursive(n)
print("Tổng của", n, "số Fibonacci đầu tiên là:", sum_recursive)

print("Không sử dụng đệ quy")
sum_recursive = sumFibonacciRecursive(n)
print("Tổng của", n, "số Fibonacci đầu tiên là:", sum_recursive)
