def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua

n = int(input("Nhập số nguyên dương n: "))
print(n, "! =", tinh_giai_thua(n))