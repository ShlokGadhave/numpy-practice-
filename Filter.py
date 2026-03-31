import numpy as np 
arr=np.array([1,2,3,4,5,6])
fa=[True,False,True,False,True,True]
new=arr[fa]
print(new)

#2 method 
a=np.array([10,20,30,40,50])
fa=a>40
new=a[fa]
print(new)