sogiay = int(input("Nhập số giây: "))

gio = sogiay // 3600
phut = (sogiay % 3600) // 60
giay = (sogiay % 3600) % 60

print(f"{gio}:{phut}:{giay}")