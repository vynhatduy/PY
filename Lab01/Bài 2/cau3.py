def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def so_nguyen_to_trong_khoang(start, end):
    for i in range(start, end + 1):
        if la_so_nguyen_to(i):
            print(i)
so_nguyen_to_trong_khoang(10, 30)