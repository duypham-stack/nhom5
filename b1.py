# bai 1 nhap 2 so a,b tim tong, hieu tich thuong cua 2 so na
try:
    a = int(input('hay nhap a:'))
    b= int(input('hay nhap b:'))
    print('tong = ', a+b)
    print('hieu =',a-b)
    print('tich =',a*b)
    print('thuong = ',a/b)
except:
    print(' du lieu nhap khong dung')
    print("abc")
finally:
    print('ket thuc chuong trinh!')
    print("aaaaaaaaaaaaaaaaaaaaaaaaa")

