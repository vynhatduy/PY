def hinh_tam_giac_roieng(so_hang):
    for i in range(1, so_hang+1):
        for j in range(1, i+1):
            if i == so_hang or j == 1 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
so_hang = int(input("Nhập số hàng của tam giác: "))
hinh_tam_giac_roieng(so_hang)

