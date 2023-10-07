from hinh_hoc import HinhHoc
class HinhChuNhat (HinhHoc):
    def __init__(self, chieuDai, chieuRong):
        super().__init__(chieuDai)
        self.rong=chieuRong
        self.dai = chieuDai
    def tinhDienTich(self):
        return self.rong*self.dai
    def Xuat(self):
        print(f"Hình chữ nhật chiều dài {self.dai}, chiều rộng{self.rong} có diện tích là : {self.tinhDienTich()}")