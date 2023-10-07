# import sqlite3


# def get_connection():
#     conn=sqlite3.connect('QLSinhVien.db')
#     return conn
# def close_connection(conn):
#     if conn:
#         conn.close()

# def read_db_version():
#     try:
#         conn=get_connection()
#         cursor=conn.cursor()
#         cursor.execute("select sqlite_version();")
#         db_version=cursor.fetchone()
#         print("Bạn đang sử dụng SQLite phiên bản: ",db_version)
#         close_connection(conn)
#     except (Exception,sqlite3.Error) as error:
#         print("Đã xảy ra lỗi. Thông tin lỗi: ",error)
# read_db_version()
import pyodbc

connect = '''DRIVER={ODBC Driver 17 for SQL Server};
            SERVER=DESKTOP-N8FRIF0;DATABASE=QLSinhVien;UID=sa;PWD=sa'''
def get_conn():
    conn=pyodbc.connect(connect)
    return conn
def close_conn(conn):
    if conn:
        conn.close()
def get_all_class():
    try:
        conn=get_conn()
        cursor=conn.cursor()
        select_query ="""select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"Danh sach ca lop la: ")
        for row in records:
            print("*"*50)
            print("Ma lop: ",row[0])
            print("Ten lop: ",row[1])
        close_conn(conn)
    except (Exception,pyodbc.Error) as error:
        print("loi tai: ",error)

def get_all():
    try:
        conn=get_conn()
        courser = conn.cursor()
        query="""SELECT a.ID,a.HoTen,b.TenLop from SinhVien a, Lop b WHERE a.MaLop=b.ID"""
        courser.execute(query)
        records = courser.fetchall()
        print(f"Danh sach sinh vien la: ")
        for row in records:
            print("Ma so: ",row[0],"\t Ho Ten: ",row[1]," "*40,"\tTen Lop: ",row[2])
        close_conn(conn)
    except (Exception,pyodbc.Error) as error:
        print("loi mo file: ",error) 

def get_class_by_id(id_class):
        try:
            conn=get_conn()
            courser=conn.cursor()
            query="select*from Lop where id=?"
            params=(id_class)
            courser.execute(query,params)
            records=courser.fetchone()
            print(f"Thông tin lớp có id ={id_class} là:")
            print("Mã lớp: ",records[0])
            print("Tên lớp: ",records[1])
            close_conn(conn)
        except(Exception,pyodbc.Error) as error:
            print("Lỗi tại: ",error)


def find_student_by_id(id):
    try:
            conn=get_conn()
            cursor=conn.cursor()
            query="select*from SinhVien where ID=?"
            params=(id)
            cursor.execute(query,params)
            records=cursor.fetchone()
            print(f"Thông tin lớp có id ={id} là:")
            print("Mã Số: ",records[0])
            print("Họ Tên: ",records[1])
            print("Mã lớp: ",records[2])
            close_conn(conn)
    except(Exception,pyodbc.Error) as error:
            print("Lỗi tại: ",error)

def get_all_student_by_class(id:int=None,*,ten:str=None):
    kq:str
    try:
        conn=get_conn()
        cursor=conn.cursor()
        
        if id is not None:
             kq=id
             query = 'select * from SinhVien a,Lop b where a.MaLop=b.ID and a.MaLop =?'
        else:
             kq=ten
             query = 'select * from SinhVien a,Lop b where a.MaLop=b.ID and b.TenLop like "% ? %" '
        cursor.execute(query,kq)
        records=cursor.fetchall()
        print(f"Danh sach sinh vien la: ")
        for row in records:
            print("Ma so: ",row[0],"\t Ho Ten: ",row[1]," "*40,"\tTen Lop: ",row[2])
        close_conn(conn)
    except(Exception,pyodbc.Error) as error:
        print("Loi tai: ",error)
def find_student(id:int,Ten:str):
    try:
        conn=get_conn()
        cursor=conn.cursor()
        query=f"""SELECT * FROM SinhVien a, Lop b WHERE a.MaLop=b.ID and b.ID = {int(id)} and a.HoTen like '%{Ten}%'"""
        cursor.execute(query)
        records = cursor.fetchall()
        print(f"Danh sach sinh vien la co ten {Ten} ma lop {id} la : ")
        print("Ma so \t HoTen"," \t\t","Ma lop")
        for row in records:
            print(row[0],"\t",row[1]," \t\t",row[2])
        close_conn(conn)
    except(Exception,pyodbc.Error) as error:
          print("Lỗi tai: ",error)
# def insert_class(class_name):
#      try:
#         conn=get_conn()
#         cursor= conn.cursor()
        
get_all_class()
get_all()
get_class_by_id(2)
find_student_by_id(12)
get_all_student_by_class(2)
find_student(3,'Trung')
