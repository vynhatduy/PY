from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien
from datetime import datetime
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
            return DanhSachSV([sv for sv in self.dssv if isinstance(sv,SinhVienChinhQuy)])
        return DanhSachSV([sv for sv in self.dssv if isinstance(sv,SinhVienPhiCQ)])
    def timSV_coDiemRL_Tren80(self,drl:int):
        # kq =[]
        # for sv in self.dssv:
        #     if  isinstance(sv,SinhVienChinhQuy) and sv._diemRL >=drl:
        #         kq.append(sv)
        # return kq

            return DanhSachSV([sv for sv in self.dssv if isinstance(sv,SinhVienChinhQuy) and sv._diemRL >= drl])
        
    def timSV_coTrinhDoCaoDang_truoc_ngay(self, trinhdo:str,ngaySinh:datetime):
     
            return DanhSachSV([sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ) and sv.trinhDo == trinhdo and sv._ngaySinh <= ngaySinh])
        