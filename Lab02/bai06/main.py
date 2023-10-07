from hinh_hoc import HinhHoc
from hinh_chu_nhat import HinhChuNhat
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from loai_hinh import LoaiHinh
from ds_hinh_hoc import DanhSachHinhHoc
import math

ht1=HinhTron(5)
ht2=HinhTron(10)
ht3=HinhTron(2)
ht4=HinhTron(8)
hv1=HinhVuong(2)
hv2=HinhVuong(3)
hv3=HinhVuong(8)
hv4=HinhVuong(1)
hcn1=HinhChuNhat(3,4)
hcn2=HinhChuNhat(8,1)
hcn3=HinhChuNhat(10,5)
hcn4=HinhChuNhat(7,16)

dshh=DanhSachHinhHoc()

dshh.themHH(ht1)
dshh.themHH(ht2)
dshh.themHH(ht3)
dshh.themHH(ht4)
dshh.themHH(hv1)
dshh.themHH(hv2)
dshh.themHH(hv3)
dshh.themHH(hv4)
dshh.themHH(hcn1)
dshh.themHH(hcn2)
dshh.themHH(hcn3)
dshh.themHH(hcn4)

dshh.xuat()
print("Hình học có diện tích lớn nhất : ===================>")
S_max = dshh.timHinhCoDienTichLonNhat()
S_max.Xuat()

print("Hình có diện tích nhỏ nhất : ===================>")
S_min = dshh.timHinhCoDienTichNhoNhat()
S_min.Xuat()

print("Hình tròn có diện tích nhỏ nhất : ===================>")
HT_min=dshh.timHinhTronNhoNhat()
HT_min.Xuat()

print("Hình tròn có diện tích lớn nhất : ===================>")
HT_max = dshh.timHinhTronLonNhat()
HT_max.Xuat()

print("Săp danh sách giảm theo diện tích : ===================>")
dshh.sapGiamTheoDienTich()
dshh.xuat()

print("Đếm số lượng hình theo kiểu loại : ===================> ")
soHinhTron=dshh.DemSoLuongHinh(HinhTron)
print(f"Số lượng hình tròn là {soHinhTron}")
soHinhVuong=dshh.DemSoLuongHinh(HinhVuong)
print(f"Số lượng hình vuông là {soHinhVuong}")
soHinhCn=dshh.DemSoLuongHinh(HinhTron)
print(f"Số lượng hình chữ nhật là {soHinhCn}")

print("Tính tổng diện tích có trong danh sách : ===================>")
kq = dshh.tongDienTich()
print("Tổng diện tích trong danh sách là: ",kq)

print("Tìm Hình có diện tích lớn nhất theo từng kiểu : ===================>")
kq1 =dshh.timHinhCoDienTichLonNhatTheoLoai(HinhTron)
print("Hình tròn có diện tích lớn nhất là ")
kq1.Xuat()
kq2 =dshh.timHinhCoDienTichLonNhatTheoLoai(HinhVuong)
print("Hình vuông có diện tích lớn nhất là ")
kq2.Xuat()
kq3 =dshh.timHinhCoDienTichLonNhatTheoLoai(HinhChuNhat)
print("Hình chữ nhật có diện tích lớn nhất là ")
kq3.Xuat()

print("Tìm vị trí của hình : ===================>")
vt=dshh.timVTCuaHinh(HinhTron)
for ht in vt:
    print("Vị trí của hình tròn là: ",ht+1)
vt=dshh.timVTCuaHinh(HinhVuong)
for hv in vt:
    print("Vị trí của hình vuông là: ",hv+1)
    vt=dshh.timVTCuaHinh(HinhChuNhat)
for hcn in vt:
    print("Vị trí của hình chũ nhật là: ",hcn+1)

print("Xóa vị trí của hình : ===================>\n")
kq= dshh.xoaHinhHoc(5)
if kq == True:
    print("Đã Xóa Hình khỏi danh sách")
    dshh.xuat()
else:
    print("Chưa xóa được hình khỏi danh sách")
    dshh.xuat()

print("Tìm hình theo diện tích")
hinh = dshh.timHinhTheoDienTich(64.0)
hinh.Xuat()


print("Xóa một hình khỏi danh sách\n")
kq = dshh.xoaHinhHoc(HinhTron)
if kq==True:
    print("Đã xóa thành công ")
    dshh.xuat()
else:
    print("Hình chưa được xóa")
    dshh.xuat()

print("\n Xóa tất cả hình theo loại: \n")
kq = dshh.xoaHinhTheoLoai(HinhTron)
if kq == True:
    print("đã xóa tất cả hình tròn ")
    dshh.xuat()
else:
    print("lỗi")

print("\nXuất hình theo chiều tăng: \n")
kq =dshh.xuatHinhTheoChieuTangGiam(HinhVuong,False)
for i in kq:
    i.Xuat()

print("\nXuất hình theo chiều giảm: \n")
kq =dshh.xuatHinhTheoChieuTangGiam(HinhVuong,True)
for i in kq:
    i.Xuat()

print("\n Tổng diện tích của hình theo loại: \n")
kq = dshh.tinhTongDTTheoKieuHinh(HinhTron)
print("tổng diện tích các hình chữ nhật là: ",kq)