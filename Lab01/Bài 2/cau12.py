print('a')
print("cách 1")
def print_odd_not_divisible_by_5(arr):
    for num in arr:
        if num % 2 != 0 and num % 5 != 0:
            print(num)
print("cách 2")
def print_odd_not_divisible_by_5(arr):
    odd_not_divisible_by_5 = [num for num in arr if num % 2 != 0 and num % 5 != 0]
    print(odd_not_divisible_by_5)

print('b')
print("cách 1")
def print_fibonacci(arr):
    fib = [0, 1]
    while fib[-1] <= max(arr):
        fib.append(fib[-1] + fib[-2])

    for num in arr:
        if num in fib:
            print(num)
print("cách 2")
def print_fibonacci(arr):
    fib = [0, 1]
    while fib[-1] <= max(arr):
        fib.append(fib[-1] + fib[-2])

    fibonacci_nums = [num for num in arr if num in fib]
    print(fibonacci_nums)


print('c')
print("cách 1")
def find_largest_prime(arr):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = None
    for num in arr:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    return largest_prime
print("cách 2")
def find_largest_prime(arr):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_nums = [num for num in arr if is_prime(num)]
    largest_prime = max(prime_nums) if prime_nums else None
    return largest_prime

print('d')
print("cách 1")
def find_smallest_fibonacci(arr):
    fib = [0, 1]
    while fib[-1] < min(arr):
        fib.append(fib[-1] + fib[-2])

    smallest_fibonacci = None
    for num in arr:
        if num in fib:
            if smallest_fibonacci is None or num < smallest_fibonacci:
                smallest_fibonacci = num
    return smallest_fibonacci
print("cách 2")
def find_smallest_fibonacci(arr):
    fib = [0, 1]
    while fib[-1] < min(arr):
        fib.append(fib[-1] + fib[-2])

    fibonacci_nums = [num for num in arr if num in fib]
    smallest_fibonacci = min(fibonacci_nums) if fibonacci_nums else None
    return smallest_fibonacci

print('e')
print("cách 1")
def calculate_average_odd(arr):
    odd_nums = [num for num in arr if num % 2 != 0]
    average = sum(odd_nums) / len(odd_nums)
    return average
print("cách 2")
def calculate_average_odd(arr):
    odd_nums = [num for num in arr if num % 2 != 0]
    average = sum(odd_nums) / len(odd_nums) if odd_nums else 0
    return average

print('f')
print("cách 1")
def calculate_product_odd_not_divisible_by_3(arr):
    product = 1
    for num in arr:
        if num % 2 != 0 and num % 3 != 0:
            product *= num
    return product
print("cách 2")
def calculate_product_odd_not_divisible_by_3(arr):
    odd_not_divisible_by_3 = [num for num in arr if num % 2 != 0 and num % 3 != 0]
    product = 1
    for num in odd_not_divisible_by_3:
        product *= num
    return product

print('g')
print("cách 1")
def swap_elements(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr
print("cách 2")
def swap_elements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

print('h')
print("cách 1")
def reverse_elements(arr):
    reversed_arr = arr[::-1]
    return reversed_arr
print("cách 2")
def reverse_elements(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print('i')
print("cách 1")
def print_second_largest(arr):
    max1 = max2 = float('-inf')
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num != max1 and num > max2:
            max2 = num
    print(max2)
print("cách 2")
def print_second_largest(arr):
    sorted_unique_nums = sorted(list(set(arr)), reverse=True)
    if len(sorted_unique_nums) > 1:
        second_largest = sorted_unique_nums[1]
        print(second_largest)
    else:
        print("No second largest number")

print('j')
print("cách 1")
def calculate_sum_of_digits(arr):
    sum_of_digits = 0
    for num in arr:
        str_num = str(num)
        for digit in str_num:
            sum_of_digits += int(digit)
    return sum_of_digits
print("cách 2")
def calculate_sum_of_digits(arr):
    sum_of_digits = 0
    for num in arr:
        sum_of_digits += sum(int(digit) for digit in str(num))
    return sum_of_digits

print('k')
print("cách 1")
def count_occurrences(arr, num):
    count = 0
    for n in arr:
        if n == num:
            count += 1
    return count
print("cách 2")
def count_occurrences(arr, num):
    count = arr.count(num)
    return count

print('l')
print("cách 1")
def print_nums_with_n_occurrences(arr, n):
    unique_nums = set(arr)
    for num in unique_nums:
        if arr.count(num) == n:
            print(num)
print("cách 2")
from collections import Counter

def print_nums_with_n_occurrences(arr, n):
    counter = Counter(arr)
    nums_with_n_occurrences = [num for num, count in counter.items() if count == n]
    print(nums_with_n_occurrences)

print('m')
print("cách 1")
def print_nums_with_highest_occurrences(arr):
    counter = Counter(arr)
    max_occurrences = max(counter.values())
    nums_with_max_occurrences = [num for num, count in counter.items() if count == max_occurrences]
    print(nums_with_max_occurrences)
print("cách 2")
def print_nums_with_highest_occurrences(arr):
    counter = Counter(arr)
    max_occurrences = max(counter.values())
    nums_with_max_occurrences = [num for num in arr if counter[num] == max_occurrences]
    print(nums_with_max_occurrences)