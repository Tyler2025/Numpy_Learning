import pandas as pd
t1 = pd.Series([1,2,3])
print(t1)

t2 = pd.Series([2,3,4,5],index=['a','b','c','d'])
print(t2)

temp_dict = {'name':'lishan','gender':'female','age':20,'tel':10086}
t3 = pd.Series(temp_dict)
print(t3)
print(t3.index)
print(t3.values)
for i in t3.values:
	print(i)


print(t3[:3])
print(t3[1,2,3])
