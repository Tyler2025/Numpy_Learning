#coding:utf-8

import numpy as np
import random

#创建数组
t1 = np.array([1,2,3])
print(t1)

t2 = np.array(range(1,10))
print(t2)

t3 = np.arange(1,10,2)
print(t3)
print(t3.dtype)

#指定改变数据类型
t4 = np.arange(1,5,dtype="u1")
print(t4)
print(t4.dtype)

t4 = t4.astype("u2")#调用方法后要再次赋值
print(t4.dtype)

#Numpy的小数
t5 = [random.random() for i in range(10)]
print(t5)

t5 = np.round(t5,3)#保留3位
print(t5)
