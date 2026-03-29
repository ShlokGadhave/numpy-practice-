import numpy as np 
arr1=np.array([[20,30],[30,40]])
arr2=np.array([[20,30],[30,40]])
print(np.concatenate([arr1,arr2]))
print(np.concatenate([arr1,arr2],axis=1)) #print on the horizontal axis 
