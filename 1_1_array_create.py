#coding:utf-8

import numpy as np
import random

#��������
t1 = np.array([1,2,3])
print(t1)

t2 = np.array(range(1,10))
print(t2)

t3 = np.arange(1,10,2)
print(t3)
print(t3.dtype)

#ָ���ı���������
t4 = np.arange(1,5,dtype="u1")
print(t4)
print(t4.dtype)

t4 = t4.astype("u2")#���÷�����Ҫ�ٴθ�ֵ
print(t4.dtype)

#Numpy��С��
t5 = [random.random() for i in range(10)]
print(t5)

t5 = np.round(t5,3)#����3λ
print(t5)
