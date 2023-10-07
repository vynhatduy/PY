import math

def tinh_tong_can_bac_2(n):
    tong = 0
    for i in range(1, n+1):
        tong += math.sqrt(i)
    return tong

n = int(input("Nhập số nguyên n: "))
tong_can_bac_2 = tinh_tong_can_bac_2(n)
print(f"Tổng căn bậc 2 của {n} số nguyên đầu tiên là {tong_can_bac_2}")

