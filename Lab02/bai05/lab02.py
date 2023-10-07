# Bài 1+2

import datetime

class SinhVien:
    truong ="Đại học đà lạt"
    def __init__(self, maSo:int, hoTen:str, ngaySinh:datetime) -> None:
        
        self.__maSo=maSo
        self.__hoTen=hoTen
        self.__ngaySinh=ngaySinh
    @property
    def maSo(self):
        return self._maSo
    @maSo.setter
    def maSo(self,maso):
        if self.laMaSoHopLe(maso):
            self._maSo=maso
    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso))==7
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong=tenmoi
    def __str__(self)-> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")
# class DanhSachSV:
#     def __init__(self) -> None:
#         self.dssv=[]
#     def themSinhVien(self,sv:SinhVien):
#         self.dssv.append(sv)
#     def xuat(self):
#         for sv in self.dssv:
#             print(sv)
#     def timSVTheoMssv(self,mssv:int):
#         return [ sv for sv in self.dssv if sv.mssv == mssv]
#     def timVTsvTheoMssv(self,mssv:int):
#         for i in range(len(self.dssv)):
#             if self.dssv[i].mssv==mssv:
#                 return i
#         return -1
#     def xoaSVTheoMssv(self,maSo:int) -> bool:
#         vt=self.timSVTheoMssv(maSo)
#         if vt != -1:
#             del self.dssv[vt]
#             return True
#         else:
#             return False
#     def timSVTheoTen(self,ten:str):
#         pass
#     def timSVSinhTruocNgay(self,ngay:datetime):
#         pass
#     def docfile(self):
#         f=open("dssv.txt","r")
#         for x in f:
#             self.dssv.append(x)
#     def sapXepSVTangTheoTen(self):
#         dssv_tang=sorted(self.dssv.hoTen)
#     def sapXepSVGiamTheoTen(self):
#         dssv_giam=sorted(self.dssv.hoTen,reverse=True)
    


#-------------------- Bài 3--------------
# class PhanSo:
#     def __init__(self, tu_so: int, mau_so: int) -> None:
#         self.tu_so = tu_so
#         self.mau_so = mau_so
#     def rutGon(self):
#         ucln = math.gcd(self.tu_so, self.mau_so)
#         self.tu_so //= ucln
#         self.mau_so //= ucln
#     def __add__(self, other):
#         new_tu_so = self.tu_so * other.mau_so + other.tu_so * self.mau_so
#         new_mau_so = self.mau_so * other.mau_so
#         return PhanSo(new_tu_so, new_mau_so)
#     def __sub__(self, other):
#         new_tu_so = self.tu_so * other.mau_so - other.tu_so * self.mau_so
#         new_mau_so = self.mau_so * other.mau_so
#         return PhanSo(new_tu_so, new_mau_so)
#     def __mul__(self, other):
#         new_tu_so = self.tu_so * other.tu_so
#         new_mau_so = self.mau_so * other.mau_so
#         return PhanSo(new_tu_so, new_mau_so)
#     def __truediv__(self, other):
#         new_tu_so = self.tu_so * other.mau_so
#         new_mau_so = self.mau_so * other.tu_so
#         return PhanSo(new_tu_so, new_mau_so)
#     def __str__(self):
#         return f"{self.tu_so}/{self.mau_so}"
# a = PhanSo(2,3)
# # a.tu_so = 2
# # a.mau_so = 3
# b = PhanSo(3,5)
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")



# #----------- bài 4 --------------
# class PhanSo:
#     def __init__(self, tu=0, mau=1):
#         self.tu = tu
#         self.mau = mau
#     def nhapPhanSo(self):
#         self.tu = int(input("Nhập tử số: "))
#         self.mau = int(input("Nhập mẫu số: "))
#     def xuatPhanSo(self):
#         print(self.tu, "/", self.mau)
# class DanhSachPhanSo:
#     def __init__(self):
#         self.ds = []
#     def themPhanSo(self, phanSo):
#         self.ds.append(phanSo)
#     def demSoPhanSoAm(self):
#         dem = 0
#         for phanSo in self.ds:
#             if phanSo.tu * phanSo.mau < 0:
#                 dem += 1
#         return dem
#     def timPhanSoDuongNhoNhat(self):
#         phanSoMin = None
#         for phanSo in self.ds:
#             if phanSo.tu * phanSo.mau > 0:
#                 if phanSoMin is None or phanSo.tu / phanSo.mau < phanSoMin.tu / phanSoMin.mau:
#                     phanSoMin = phanSo
#         return phanSoMin
#     def timViTriCuaPhanSo(self, x):
#         viTri = []
#         for i, phanSo in enumerate(self.ds):
#             if phanSo.tu == x.tu and phanSo.mau == x.mau:
#                 viTri.append(i)
#         return viTri
#     def tongCacPhanSoAm(self):
#         tong = 0
#         for phanSo in self.ds:
#             if phanSo.tu * phanSo.mau < 0:
#                 tong += phanSo.tu / phanSo.mau
#         return tong
#     def xoaPhanSo(self, x):
#         self.ds = [phanSo for phanSo in self.ds if (phanSo.tu != x.tu or phanSo.mau != x.mau)]
#     def xoaTatCaPhanSoCoTuLa(self, x):
#         self.ds = [phanSo for phanSo in self.ds if phanSo.tu != x]
#     def sapXepPhanSo(self, kieu):
#         self.ds.sort(key=lambda phanSo: (phanSo.tu / phanSo.mau) if kieu == "tang" else -(phanSo.tu / phanSo.mau))
# danhSach = DanhSachPhanSo()
# danhSach.themPhanSo(PhanSo(1, 2))
# danhSach.themPhanSo(PhanSo(-25, 33))
# danhSach.themPhanSo(PhanSo(3, 4))
# danhSach.themPhanSo(PhanSo(100, 355))
# danhSach.themPhanSo(PhanSo(20, -63))
# print("Số phân số âm trong mảng:", danhSach.demSoPhanSoAm())
# phanSoMin = danhSach.timPhanSoDuongNhoNhat()
# if phanSoMin is not None:
#     print("Phân số dương nhỏ nhất:")
#     phanSoMin.xuatPhanSo()
# x = PhanSo(3, 4)
# print("Vị trí của phân số", end=" ")
# x.xuatPhanSo()
# print("trong mảng:", danhSach.timViTriCuaPhanSo(x))
# print("Tổng các phân số âm trong mảng:", danhSach.tongCacPhanSoAm())
# x = PhanSo(1, 2)
# print("Xóa phân số", end=" ")
# x.xuatPhanSo()
# danhSach.xoaPhanSo(x)
# print("Mảng sau khi xóa:")
# for phanSo in danhSach.ds:
#     phanSo.xuatPhanSo()
# x = 2
# print("Xóa tất cả phân số có tử là", x)
# danhSach.xoaTatCaPhanSoCoTuLa(x)
# print("Mảng sau khi xóa:")
# for phanSo in danhSach.ds:
#     phanSo.xuatPhanSo()
# print("Sắp xếp phân số theo chiều tăng:")
# danhSach.sapXepPhanSo("tang")
# for phanSo in danhSach.ds:
#     phanSo.xuatPhanSo()
# print("Sắp xếp phân số theo chiều giảm:")
# danhSach.sapXepPhanSo("giam")
# for phanSo in danhSach.ds:
#     phanSo.xuatPhanSo()


#------------- bài 5 ----------
from datetime import datetime
class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self,maSo:int,hoTen:str,ngaySinh:datetime) -> None:
        self.maSo=maSo
        self.hoTen=hoTen
        self.ngaySinh=ngaySinh
    @property
    def hoTen(self):
        return self.hoTen
    @hoTen.setter
    def hoTen(self,hoTen:str):
        self.hoTen=hoTen
    @property
    def mssv(self):
        return self.maSo
    @mssv.setter
    def mssv(self,ms:int):
        if self.ktMsHopLe(ms):
            self.maSo=ms
    @staticmethod
    def ktMsHopLe(mssv:int):
        return len(str(mssv))==7
    def __str__(self) -> str:
        return f"{self.maSo}\t{self.hoTen}\t{self.ngaySinh}"
#from sinh_vien import SinhVien
from datetime import datetime
class SinhVienChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime,diemRL:int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.diemRL=diemRL
    def __str__(self) -> str:
        return super().__str__()+f"\t{self.diemRL}"

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime,trinhdo:str,tgdt:int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.thoiGianDaoTao=tgdt
        self.trinhDo=trinhdo
    def __str__(self) -> str:
        return super().__str__()+f"{self.trinhDo}\t{self.thoiGianDaoTao}"


class DanhSachSV:
    def __init__(self) -> None:
        self.dssv=[]
    def themSV(self,sv:SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def timSVTheoMS(self,ms:str):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv==ms:
                return i
        else:
            return -1
    def timSVTheoLoai(self, loai:str):
        if loai=="chinhquy":
            return [sv for sv in self.dssv if isinstance(sv,SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv,SinhVienPhiCQ)]
    def timSV_coDiemRL_Tren80(self,diemRL:int):
        if diemRL >= 80:
            return [sv for sv in self.dssv if isinstance(sv,SinhVienChinhQuy)]
        return -1
    def timSV_coTrinhDoCaoDang_truoc_ngay(self, trinhdo:str,ngaySinh:datetime):
        if trinhdo =="cao đẳng" and ngaySinh<= "15/8/1999":
            return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]
        return -1
    sv1 = SinhVienChinhQuy(1957690,"Trần Văn A", datetime.strptime("23/6/1999","%d/%m/%Y"),80)
    sv2 = SinhVienChinhQuy(1957691,"Nguyễn văn C",datetime.strptime("5/12/1999","%d/%m/%Y"),90)
    sv3 = SinhVienPhiCQ(1957692,"Thái Thị Thu",datetime.strptime("15/8/1998","%d/%m/%Y"),"cao đẳng",2)
    sv4 = SinhVienPhiCQ(2000324,"Trần Thanh Tâm",datetime.strptime("27/8/2000","%d/%m/%Y"),"cao đẳng",2)
    sv5 = SinhVienPhiCQ(2004544,"Nguyễn Thanh Trà",datetime.strptime("17/5/1999","%d/%m/%Y"),"trung cấp",2.5)
    sv6 = SinhVienChinhQuy(2004567,"Nguyễn Thành Nam",datetime.strptime("7/12/1999","%d/%m/%Y"),60)
    sv7 = SinhVienPhiCQ(2004545,"Nguyễn Thanh Thanh",datetime.strptime("29/10/1999","%d/%m/%Y"),"trung cấp",2.5)
    sv8 = SinhVienChinhQuy(2004679,"Võ Hoài Nam",datetime.strptime("4/1/2000","%d/%m/%Y"),70)
    
    dssv = DanhSachSV()
    dssv.themSV(sv1)
    dssv.themSV(sv2)
    dssv.themSV(sv3)
    dssv.themSV(sv4)
    dssv.themSV(sv5)
    dssv.themSV(sv6)
    dssv.themSV(sv7)
    dssv.themSV(sv8)
    dssv.xuat()

