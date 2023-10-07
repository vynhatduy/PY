import math

def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        return "Phương trình vô nghiệm"
    
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

ket_qua = giai_phuong_trinh_bac_hai(a, b, c)

print("Kết quả: ", ket_qua)

