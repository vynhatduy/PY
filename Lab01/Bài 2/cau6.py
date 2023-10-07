def fibonacci_recursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def sum_of_n_fibonacci_recursion(n):
    sum = 0
    for i in range(1, n+1):
        sum += fibonacci_recursion(i)
    return sum


def sum_of_n_fibonacci_iteration(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_numbers = [0, 1]  # danh sách lưu trữ các số Fibonacci
    sum = 0
    for i in range(2, n+1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])
        sum += fib_numbers[i]

    return sum

n = int(input("Nhập số lượng số Fibonacci muốn tính tổng: "))
print("Tổng", n, "số Fibonacci đầu tiên (không dùng đệ quy):", sum_of_n_fibonacci_iteration(n))


print("Tổng", n, "số Fibonacci đầu tiên (dùng đệ quy):", sum_of_n_fibonacci_recursion(n))

