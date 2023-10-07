from hinh_hoc import HinhHoc
class HinhTron(HinhHoc):
    def __init__(self,banKinh) -> None:
        super().__init__(banKinh)
        self.banKinh=banKinh
    def tinhDienTich(self):
        return 3.14*self.banKinh**2
    def Xuat(self):
        print(f"Hinh Tròn bán kính {self.banKinh} có diện tích là {self.tinhDienTich()}")