#coding:utf-8

import numpy as np
#�鿴��״
t1 = np.array([[1,2,4],[5,3,6]])
print(t1.shape)
print(t1)
#�ı���״
t2 = t1.reshape((3,2))
print(t2.shape)
print(t2)

t3 = t1.flatten()
print(t3.shape)
print(t3)
#�㲥����
print(t3*3)
print(t3-4)

t4 = np.arange(1,5).reshape(4,1,1)
print(t4.shape)
print(t4)
#(3,2)��(4,1,1)������
print(t4*t2)
