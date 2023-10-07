import sys
import datetime
from math import pi

print('1')
print('''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are''')

print('2')
print("Python version",sys.version)
print("Python info", sys.version_info)

print('3')
print("ngày giờ hiện tài: ", datetime.datetime.now())

print('4')
r = float(input ("Nhập bán kính hình tròn : "))
print ("Diện tích hình tròn có bán kính  " + str(r) + " là : " + str(pi * r**2))

print('5')
ho = input("Nhập họ : ")
ten = input("Nhập tên : ")
print ("Hello  " + ho + " " + ten)

print('6')
values = input("Nhập vào các số : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

print('7')
filename = input("Nhập tên file: ")
f_extns = filename.split(".")
print ("Phần mở rộng của file là : " + repr(f_extns[-1]))

print('8')
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))

print('9')
exam_st_date = (11,12,2014)
print( "định dạng ngày sẽ là : %i / %i / %i"%exam_st_date)

print('10')
a = int(input("Nhập vào 1 số nguyên : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

print('11')
print(abs.__doc__)

print('12')
import calendar
y = int(input("Nhập vào năm : "))
m = int(input("Nhập vào tháng : "))
print(calendar.month(y, m))

print('13')
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

print('14')
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

print('15')
r= 6.0
V= 4.0/3.0*pi* r**3
print('Thể tích của hình cầu là: ',V)

print('16')
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))

print('17')
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))

print('18')
def sum_thrice(x, y, z):
     sum = x + y + z
     if x == y == z:
      sum = sum * 3
     return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

print('19')
def new_string(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text
  return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty")) 

print('20')
def larger_string(text, n):
   result = ""
   for i in range(n):
      result = result + text
   return result
print(larger_string('abc', 2))
print(larger_string('.py', 3)) 

print('21')
num = int(input("Nhập số nguyên: "))
mod = num % 2
if mod > 0:
    print("là số lẽ")
else:
    print("là số chẵn")

print('22')
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1
  return count
print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))

print('23')
def substring_copy(text, n):
  flen = 2
  if flen > len(text):
    flen = len(text)
  substr = text[:flen]
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));

print('24')
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))

print('25')
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
