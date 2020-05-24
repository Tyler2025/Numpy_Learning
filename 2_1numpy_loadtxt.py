import numpy as np
import random
'''
#注意此处在win中需要加上r以保持字符串原意

GB_file_path = "C:\\Users\\Tyler Leigh\\Desktop\\Machine Learning\\numpy_learning\\Numpy_Learning\\data\\youtube_video_data\\GB_video_data_numbers.csv"
US_file_path = "C:\\Users\\Tyler Leigh\\Desktop\\Machine Learning\\numpy_learning\\Numpy_Learning\\data\\youtube_video_data\\US_video_data_numbers.csv"

#读取csv文件
data = np.loadtxt(GB_file_path,dtype=int,delimiter=",")
print(data)
print("*"*100)
print(data.transpose())


#索引 ctrl+E注释
a = np.arange(100).reshape(10,10)

print(a)

print(a[0])
print(a[:,0])

print(a[1:5,3:6])#取交点
print(a[[1,2,3,4],[3,4,5,6]])#取不相邻的元素

#编辑元素
b = np.arange(1,101,2).reshape(5,10)
print(b)
print(b>50)
c = b[b>50]
print(c)
print(np.where(b>50,0,1))
print(b.clip(10,20))
b = b.astype(float)
print(np.count_nonzero(b!=b))
b[[2,3,4],[1,0,9]]=np.nan
print(np.count_nonzero(b!=b))

#numpy中常用统计函数
t = np.arange(60).reshape(6,10)
print(t.sum(axis=0))
print(t.mean(axis=0))
print(np.median(t,axis=0))
print(t.max(axis=0))
print(t.min(axis=0))
print(t.ptp(axis=0))
print(t.std(axis=0))
#数组拼接以及其他操作
t = np.arange(30,dtype=int).reshape(3,10)
ran = np.random.randint(3,10,(3,10)).astype(int)
vertical = np.vstack((t,ran))
horizonal = np.hstack((t,ran))
print(vertical)
print('*'*100)
print(horizonal)
print('*'*100)
vertical[[1,2],:] = vertical[[2,1],:]#交换行列
vertical[:,[3,4]] = vertical[:,[4,3]]
print(vertical)
print(np.argmax(vertical,axis=0))
print(np.argmin(vertical,axis=1))
'''
#生成随机数
# ~ x = np.random.randint(-20,20,(3,4))
# ~ print(x)
# ~ x = np.random.rand(4,3)
# ~ print(x)
# ~ x = np.random.randn(4,3)
# ~ print(x)
# ~ x = np.random.randn(4,3)
# ~ print(x)
np.random.seed(2)#其后生成的随机数将是一样（次数）
print(np.random.randint(3,20,(5,5)))
print(np.random.randint(3,20,(5,5)))
