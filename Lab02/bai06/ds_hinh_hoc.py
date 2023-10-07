from hinh_hoc import HinhHoc
from loai_hinh import LoaiHinh
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from hinh_chu_nhat import HinhChuNhat
import math
import operator


class DanhSachHinhHoc:
    def __init__(self,ds=[]) -> None:
        self.dshh=list(ds)
    def themHH(self,hh:HinhHoc):
        self.dshh.append(hh)
    
    def xuat(self):
        for hh in self.dshh:
            hh.Xuat()
    
    
    def timHinhCoDienTichLonNhat(self) -> HinhHoc:
        max_s=-1
        hinhLonNhat = None

        for hinh in self.dshh:
            s = hinh.tinhDienTich()
            if s > max_s:
                max_s = s
                hinhLonNhat = hinh
        return DanhSachHinhHoc(hinhLonNhat)
         

    def timHinhCoDienTichNhoNhat(self) ->HinhHoc:
        min_s = 100000
        hinhNhoNhat = None
        for hinh in self.dshh:
            s = hinh.tinhDienTich()
            if s < min_s:
                min_s=s
                hinhNhoNhat=hinh
        return DanhSachHinhHoc(hinhNhoNhat)
    

    def timHinhTronNhoNhat(self) -> HinhHoc:
        min_s =10000
        hinhTronNhoNhat = None

        for i in self.dshh:
            if type(i) == HinhTron:
                s = i.tinhDienTich()
                if min_s>s:
                    min_s=s
                    hinhTronNhoNhat=i
        return DanhSachHinhHoc (hinhTronNhoNhat)
    
    def timHinhTronLonNhat(self) -> HinhTron:
        max_s = -1
        hinhTronLonNhat = None

        for hinh in self.dshh:
            if isinstance(hinh,HinhTron):
                s=hinh.tinhDienTich()
                if s>max_s:
                    max_s=s
                    hinhTronLonNhat=hinh
        return DanhSachHinhHoc (hinhTronLonNhat)
    
    def sapGiamTheoDienTich(self):
        self.dshh.sort(key=lambda x: x.tinhDienTich(), reverse=True)

    def DemSoLuongHinh (self, kieu:LoaiHinh):
        soLuong = 0
        for hinh in self.dshh:
            if isinstance(hinh, kieu):
                soLuong+=1
        return soLuong
    
    def tongDienTich(self):
        dienTich = 0
        for hinh in self.dshh:
            s = hinh.tinhDienTich()
            dienTich+=s
        return dienTich
    
    def timHinhCoDienTichLonNhatTheoLoai(self,kieu:LoaiHinh)-> HinhHoc:
        max_s =-1
        loaiHinh =None
        for hinh in self.dshh:
            if isinstance( hinh, kieu):
                s= hinh.tinhDienTich()
                if s>max_s:
                    max_s=s
                    loaiHinh=hinh
        return loaiHinh
    
    def timVTCuaHinh(self, h:HinhHoc):
        kq =[]
        for i in range(len(self.dshh)):
            if isinstance(self.dshh[i],h):
                kq.append(i)   
        return kq
        
    def xoaTaiViTri(self,vt:int) ->bool:
        for i in range(len(self.dshh)):
            if i == vt:
                self.dshh.remove(i)
                return 1
        else:
            return -1
    
    def timHinhTheoDienTich(self, dt:float)->HinhHoc:
        hh = None
        for i in self.dshh:
            if i.tinhDienTich()==dt:
                hh = i
        return hh
    
    def xoaHinhHoc(self,hh:HinhHoc)->bool:
        for i in self.dshh:
            if isinstance(i,HinhHoc):
                self.dshh.remove(i)
                return True
        return False
        
    def xoaHinhTheoLoai(self, kieu:LoaiHinh) -> bool:
        for hinh in self.dshh:
            if isinstance(hinh,kieu):
                self.dshh.remove(hinh)
        for hinh in self.dshh:
            if isinstance(hinh,kieu):
                return False
        return True
    def xuatHinhTheoChieuTangGiam(self, kieu:LoaiHinh,Tang:bool):
        kq =[]
        for hinh in self.dshh:
            if isinstance(hinh,kieu):
                kq.append(hinh)
        if Tang==True:
            kq.sort(key=lambda x:x.tinhDienTich())
        else:
            kq.sort(key=lambda x:x.tinhDienTich(),reverse=True)
        return kq
    

    def tinhTongDTTheoKieuHinh(self, kieu:LoaiHinh):
        kq = 0.0
        for i in range(len(self.dshh)):
            if isinstance(self.dshh[i],kieu):
                kq += self.dshh[i].tinhDienTich()
        return kq
        
    