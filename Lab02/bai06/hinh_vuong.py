from hinh_chu_nhat import HinhChuNhat
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh,canh)
    def Xuat(self):
        print(f"Hình vuông có cạnh {self.canh} có diện tích là {self.tinhDienTich()}")