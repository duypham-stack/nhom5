import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)
tongsv= in_data[:,1]
x=np.sum(tongsv)
print('Tong so sinh vien di thi :',x)
tongsvtruot= in_data[:,10]
y=np.sum(tongsvtruot)
print('So sinh vien truot :',y)
z=100-(y*100/x)
print('Ti le sinh vien qua mon la: ',z, '%')
L1=in_data[:,11]
L2=in_data[:,12]
tx1=in_data[:,13]
tx2=in_data[:,14]
CK=in_data[:,15]
diemA = in_data[:,3]
diemBc = in_data[:,4]
diemB = in_data[:,5]
print('Tong sv:',tongsv)
print(' ')
maxa = diemA.max()
i, = np.where(diemA == maxa)
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))
plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.plot(range(len(diemBc)),diemBc,'g-',label="Diem B +")
plt.plot (range(len(diemB)),diemB,'y-',label="Diem B")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
